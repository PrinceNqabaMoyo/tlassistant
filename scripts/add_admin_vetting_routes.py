import os

admin_path = os.path.join('caps-ai-backend', 'app', 'api', 'admin.py')
with open(admin_path, 'r', encoding='utf-8') as f:
    content = f.read()

vetting_code = '''

# ============================================================================
# SUPER ADMIN ARCHETYPE & DIAGRAM VETTING WORKBENCH (RULE 0d-2 & 0d-15)
# Authenticated endpoints strictly restricted to verified platform owners:
# princenqaba@gmail.com, princenqabamoyo@outlook.com
# ============================================================================

from app.services.generator_registry import ALL_GENERATORS, generate_variant

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
    """Returns the full catalog of registered generators, their curriculum mapping, and vetting status."""
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
    vetting_summary = {'total_catalog': len(catalog), 'certified': 0, 'needs_adjustment': 0, 'pending': len(catalog)}
    records = []
    try:
        db = get_firestore_client()
        docs = db.collection('archetype_vetting_records').limit(300).stream()
        for doc in docs:
            d = doc.to_dict() or {}
            d['id'] = doc.id
            records.append(d)
            if d.get('verdict') == 'CERTIFIED':
                vetting_summary['certified'] += 1
                vetting_summary['pending'] = max(0, vetting_summary['pending'] - 1)
            elif d.get('verdict') == 'NEEDS_ADJUSTMENT':
                vetting_summary['needs_adjustment'] += 1
                vetting_summary['pending'] = max(0, vetting_summary['pending'] - 1)
    except Exception as fe:
        print(f"[Admin Vetting] Firestore read notice: {fe}")

    return jsonify({
        'catalog': catalog,
        'summary': vetting_summary,
        'recent_reviews': records[:25],
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
    topic = body.get('topic')
    if not topic or topic not in ALL_GENERATORS:
        return jsonify({'error': f'Invalid or unregistered topic generator: {topic}'}), 400

    seed_val = int(body.get('seed', 1001))
    count = int(body.get('count', 1))
    subskill = body.get('subskill')
    mode = body.get('mode', 'compound')

    try:
        raw_res = generate_variant(topic, seed=seed_val, count=count, subskill=subskill, mode=mode)
        questions = []
        if isinstance(raw_res, list):
            questions = raw_res
        elif isinstance(raw_res, dict):
            questions = raw_res.get('questions', [raw_res])
        else:
            questions = [raw_res]

        return jsonify({
            'topic': topic,
            'seed': seed_val,
            'questions': questions,
            'count': len(questions),
        }), 200
    except Exception as ge:
        import traceback
        traceback.print_exc()
        return jsonify({'error': f'Generator execution failed: {str(ge)}'}), 500

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
    topic = body.get('topic')
    seed = body.get('seed')
    verdict = body.get('verdict', 'CERTIFIED')
    notes = body.get('notes', '')
    diagram_rating = body.get('diagram_rating', 5)
    rubric_rating = body.get('rubric_rating', 5)
    hints_rating = body.get('hints_rating', 5)

    if not topic:
        return jsonify({'error': 'Missing required topic.'}), 400

    doc_id = f"{topic}_{seed}"
    record = {
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
'''

if 'get_vetting_catalog' not in content:
    content += vetting_code
    with open(admin_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print('Successfully added vetting endpoints to admin.py')
else:
    print('Vetting endpoints already exist in admin.py')
