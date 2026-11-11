import os
from pathlib import Path
import json
import datetime
from flask import Blueprint, jsonify, request
from app.utils.firebase_admin_client import get_firestore_client, verify_firebase_id_token

admin_bp = Blueprint('admin', __name__)

ARCHETYPES_CATALOG_PATH = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "data",
    "diagram_archetypes_catalog.json"
)

def _load_archetypes_catalog():
    if os.path.exists(ARCHETYPES_CATALOG_PATH):
        try:
            with open(ARCHETYPES_CATALOG_PATH, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return []
    return []

def _get_bearer_token():
    authorization = request.headers.get('Authorization', '')
    if not authorization.startswith('Bearer '):
        raise PermissionError('Missing Firebase bearer token.')
    token = authorization.split(' ', 1)[1].strip()
    if not token:
        raise PermissionError('Missing Firebase bearer token.')
    return token

def _verify_request_user():
    return verify_firebase_id_token(_get_bearer_token())

def _is_admin_user(user_id, email=None):
    if email in ['princenqaba@gmail.com', 'princenqabamoyo@outlook.com']:
        return True
    try:
        firestore_client = get_firestore_client()
        user_snapshot = firestore_client.collection('users').document(user_id).get()
        if not user_snapshot.exists:
            return False
        user_data = user_snapshot.to_dict() or {}
        return bool(user_data.get('isOwner') or user_data.get('isSuperAdmin') or user_data.get('role') == 'admin')
    except Exception:
        return False

@admin_bp.route('/delete-expired-solved-problems', methods=['POST'])
def delete_expired_solved_problems():
    """
    Deletes solved_freeform_problems documents where retentionDate has passed.
    Protected endpoint: Requires valid Firebase Bearer token and Admin privileges.
    """
    try:
        user_info = _verify_request_user()
        user_id = user_info.get('uid')
        email = user_info.get('email')
        if not _is_admin_user(user_id, email):
            return jsonify({'error': 'Unauthorized: Administrator privileges required.'}), 403
    except PermissionError as pe:
        return jsonify({'error': str(pe)}), 401
    except Exception as e:
        return jsonify({'error': f'Authentication failed: {str(e)}'}), 401

    print("Starting deletion of expired solved problems...")
    
    now = datetime.datetime.now(datetime.timezone.utc)
    app_id = os.getenv("FIREBASE_APP_ID", "default-app-id") 

    deleted_count = 0
    batch_size = 500 # Firestore limit for batch writes

    try:
        firestore_db = get_firestore_client()
        users_ref = firestore_db.collection('users')
        users_docs = users_ref.stream()

        for user_doc in users_docs:
            user_id = user_doc.id
            print(f"Processing user: {user_id}")
            
            problems_ref = firestore_db.collection('artifacts').document(app_id).collection('users').document(user_id).collection('solved_freeform_problems')
            query_ref = problems_ref.where('retentionDate', '<=', now.isoformat()) 

            while True:
                docs_to_delete = query_ref.limit(batch_size).stream()
                batch = firestore_db.batch()
                
                doc_count_in_batch = 0
                for doc_snapshot in docs_to_delete:
                    batch.delete(doc_snapshot.reference)
                    doc_count_in_batch += 1
                
                if doc_count_in_batch == 0:
                    break 

                batch.commit()
                deleted_count += doc_count_in_batch
                print(f"  Deleted {doc_count_in_batch} problems for user {user_id}. Total deleted: {deleted_count}")

                if doc_count_in_batch < batch_size:
                    break

        print(f"Finished deleting expired solved problems. Total deleted: {deleted_count}")
        return jsonify({"message": f"Successfully deleted {deleted_count} expired solved problems."}), 200

    except Exception as e:
        print(f"Error during deletion of expired solved problems: {e}")
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


# ============================================================================
# SUPER ADMIN ARCHETYPE & DIAGRAM VETTING WORKBENCH (RULE 0d-2 & 0d-15)
# Authenticated endpoints strictly restricted to verified platform owners:
# princenqaba@gmail.com, princenqabamoyo@outlook.com
# ============================================================================

from app.services.generator_registry import ALL_GENERATORS, generate_variant, get_topic_archetypes

def _infer_subject_and_grade(key: str) -> tuple[str, int]:
    k = key.lower()
    grade = 10
    for g in [12, 11, 10, 9, 8, 7]:
        if f"grade{g}" in k or f"gr{g}" in k or f"g{g}" in k or f"ls{g}" in k or f"ps{g}" in k or f"ns{g}" in k or f"tm{g}" in k or f"ml{g}" in k:
            grade = g
            break

    if "life_sciences" in k or k.startswith("ls") or "heart" in k or "cell" in k:
        subject = "Life Sciences"
    elif "physical_sciences" in k or k.startswith("ps") or "physics" in k or "chemistry" in k:
        subject = "Physical Sciences"
    elif "natural_sciences" in k or k.startswith("ns"):
        subject = "Natural Sciences"
    elif "technical_mathematics" in k or k.startswith("tm"):
        subject = "Technical Mathematics"
    elif "mathematical_literacy" in k or k.startswith("ml"):
        subject = "Mathematical Literacy"
    elif "accounting" in k or "ledger" in k or "journal" in k:
        subject = "Accounting"
    elif "ems" in k or "economy" in k:
        subject = "EMS"
    elif "business" in k:
        subject = "Business Studies"
    elif "math" in k or "algebra" in k or "calculus" in k or "geometry" in k:
        subject = "Mathematics"
    else:
        subject = "General Curriculum"

    return subject, grade

@admin_bp.route('/vet/catalog', methods=['GET'])
def get_vetting_catalog():
    """Returns the full catalog of registered generators, explicit diagram archetypes, and vetting status."""
    try:
        user_info = _verify_request_user()
        user_id = user_info.get('uid')
        email = user_info.get('email')
        if not _is_admin_user(user_id, email):
            return jsonify({'error': 'Unauthorized: Super Admin privileges required.'}), 403
    except PermissionError as pe:
        return jsonify({'error': str(pe)}), 401
    except Exception as e:
        return jsonify({'error': f'Authentication failed: {str(e)}'}), 401

    # Load structured curriculum topics from authoritative manifest
    curriculum_topics = []
    manifest_path = Path(__file__).parent.parent / "services" / "caps_term_registry_data.json"
    if manifest_path.exists():
        try:
            with open(manifest_path, 'r', encoding='utf-8') as mf:
                curriculum_topics = json.load(mf)
        except Exception as me:
            print(f"[Admin Vetting] Error loading curriculum manifest: {me}")

    catalog = []
    for gen_key in sorted(ALL_GENERATORS.keys()):
        subject, grade = _infer_subject_and_grade(gen_key)
        catalog.append({
            'key': gen_key,
            'subject': subject,
            'grade': grade,
            'label': gen_key.replace('_', ' ').title(),
        })

    # Fetch vetting records from Firestore if available
    records = []
    reviews_by_arch = {}
    try:
        db = get_firestore_client()
        docs = db.collection('archetype_vetting_records').limit(500).stream()
        for doc in docs:
            d = doc.to_dict() or {}
            d['id'] = doc.id
            records.append(d)
            a_id = d.get('archetype_id') or d.get('topic')
            if a_id:
                reviews_by_arch[a_id] = d
    except Exception as fe:
        print(f"[Admin Vetting] Firestore read notice: {fe}")

    # Load canonical diagram archetypes
    raw_archetypes = _load_archetypes_catalog()
    archetypes = []
    masters_map = {}

    summary = {
        'total_generators': len(catalog),
        'total_archetypes': len(raw_archetypes),
        'certified': 0,
        'needs_adjustment': 0,
        'pending': 0,
    }

    for arch in raw_archetypes:
        a_id = arch.get('archetype_id')
        review = reviews_by_arch.get(a_id) or reviews_by_arch.get(arch.get('topic'))
        verdict = review.get('verdict', 'PENDING') if review else 'PENDING'
        
        arch_entry = {
            **arch,
            'verdict': verdict,
            'last_review': review,
        }
        archetypes.append(arch_entry)

        if verdict == 'CERTIFIED':
            summary['certified'] += 1
        elif verdict == 'NEEDS_ADJUSTMENT':
            summary['needs_adjustment'] += 1
        else:
            summary['pending'] += 1

        # Group by diagram master
        d_id = arch.get('diagram_id')
        if d_id not in masters_map:
            masters_map[d_id] = {
                'diagram_id': d_id,
                'title': arch.get('title', d_id.replace('_', ' ').title()),
                'category': arch.get('category', 'Category A (Heart Standard)'),
                'archetypes': [],
            }
        masters_map[d_id]['archetypes'].append(arch_entry)

    diagram_masters = list(masters_map.values())

    return jsonify({
        'catalog': catalog,
        'curriculum_topics': curriculum_topics,
        'archetypes': archetypes,
        'diagram_masters': diagram_masters,
        'summary': summary,
        'recent_reviews': records[:30],
    }), 200

@admin_bp.route('/vet/generate', methods=['POST'])
def vet_generate():
    """Generates authentic questions across seeds for live Super Admin inspection."""
    try:
        user_info = _verify_request_user()
        user_id = user_info.get('uid')
        email = user_info.get('email')
        if not _is_admin_user(user_id, email):
            return jsonify({'error': 'Unauthorized: Super Admin privileges required.'}), 403
    except PermissionError as pe:
        return jsonify({'error': str(pe)}), 401
    except Exception as e:
        return jsonify({'error': f'Authentication failed: {str(e)}'}), 401

    body = request.get_json() or {}
    archetype_id = body.get('archetype_id')
    topic = body.get('topic')
    subskill = body.get('subskill')
    raw_seed = body.get('seed')
    seed_val = int(raw_seed) if raw_seed is not None else random.randint(1000, 999999)
    count = int(body.get('count', 1))
    mode = body.get('mode', 'compound')
    view = body.get('view')

    target_archetype = None
    if archetype_id:
        all_archs = _load_archetypes_catalog()
        for a in all_archs:
            if a.get('archetype_id') == archetype_id:
                target_archetype = a
                break

    if target_archetype:
        topic = target_archetype['topic']
        subskill = target_archetype.get('subskill_param', subskill)
        view = target_archetype.get('view', view)
        subject = target_archetype.get('subject')
        grade = str(target_archetype.get('grade'))
    else:
        subject = body.get('subject', 'Mathematics')
        grade = str(body.get('grade', '10'))

    if not topic:
        return jsonify({'error': 'Missing topic or archetype_id'}), 400

    try:
        extra_config = {'mode': mode}
        if view:
            extra_config['view'] = view

        raw_res = generate_variant(
            topic=topic,
            grade=grade,
            subject=subject,
            subskill=subskill,
            seed=seed_val,
            count=count,
            extra_config=extra_config
        )
        questions = []
        if isinstance(raw_res, list):
            questions = raw_res
        elif isinstance(raw_res, dict):
            questions = raw_res.get('questions', [raw_res])
        else:
            questions = [raw_res]

        # Tag each question with target archetype metadata
        for q in questions:
            if archetype_id:
                q['archetype_id'] = archetype_id
            if target_archetype:
                q['archetype_title'] = target_archetype.get('title')

        return jsonify({
            'archetype_id': archetype_id,
            'topic': topic,
            'subskill': subskill,
            'seed': seed_val,
            'questions': questions,
            'count': len(questions),
        }), 200
    except Exception as ge:
        import traceback
        traceback.print_exc()
        return jsonify({'error': f'Generator execution failed: {str(ge)}'}), 500

@admin_bp.route('/vet/topic-archetypes', methods=['GET'])
def get_topic_archetypes_endpoint():
    """Returns the discovered archetypes for a given topic/generator key."""
    try:
        user_info = _verify_request_user()
        user_id = user_info.get('uid')
        email = user_info.get('email')
        if not _is_admin_user(user_id, email):
            return jsonify({'error': 'Unauthorized: Super Admin privileges required.'}), 403
    except PermissionError as pe:
        return jsonify({'error': str(pe)}), 401
    except Exception as e:
        return jsonify({'error': f'Authentication failed: {str(e)}'}), 401

    topic = request.args.get('topic', '')
    grade = request.args.get('grade', '10')
    subject = request.args.get('subject', 'Mathematics')

    info = get_topic_archetypes(topic, grade=grade, subject=subject)
    return jsonify(info), 200

@admin_bp.route('/vet/save-review', methods=['POST'])
def save_vetting_review():
    """Saves a Super Admin certification or adjustment verdict to Firestore."""
    try:
        user_info = _verify_request_user()
        user_id = user_info.get('uid')
        email = user_info.get('email')
        if not _is_admin_user(user_id, email):
            return jsonify({'error': 'Unauthorized: Super Admin privileges required.'}), 403
    except PermissionError as pe:
        return jsonify({'error': str(pe)}), 401
    except Exception as e:
        return jsonify({'error': f'Authentication failed: {str(e)}'}), 401

    body = request.get_json() or {}
    archetype_id = body.get('archetype_id')
    topic = body.get('topic')
    seed = body.get('seed', 1)
    verdict = body.get('verdict', 'CERTIFIED')
    notes = body.get('notes', '')
    diagram_rating = body.get('diagram_rating', 5)
    rubric_rating = body.get('rubric_rating', 5)
    hints_rating = body.get('hints_rating', 5)

    if not archetype_id and not topic:
        return jsonify({'error': 'Missing required archetype_id or topic.'}), 400

    doc_key = archetype_id or topic
    doc_id = f"{doc_key}_{seed}"
    record = {
        'archetype_id': archetype_id,
        'topic': topic,
        'seed': seed,
        'verdict': verdict,
        'notes': notes,
        'diagram_rating': diagram_rating,
        'rubric_rating': rubric_rating,
        'hints_rating': hints_rating,
        'reviewer_email': email,
        'reviewer_id': user_id,
        'timestamp': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    }

    try:
        db = get_firestore_client()
        db.collection('archetype_vetting_records').document(doc_id).set(record, merge=True)
        return jsonify({'success': True, 'record': record}), 200
    except Exception as fe:
        return jsonify({'error': f'Failed to persist review: {str(fe)}'}), 500
