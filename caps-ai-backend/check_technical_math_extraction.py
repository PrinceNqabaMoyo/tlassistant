import os
from dotenv import load_dotenv
import google.generativeai as genai
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma
from tabulate import tabulate
from collections import defaultdict

# Load environment variables from .env file
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Configure Gemini API (needed for embeddings even if just loading Chroma)
genai.configure(api_key=GOOGLE_API_KEY)

# --- Configuration ---
CHROMA_DB_DIR = "chroma_db_langchain"
COLLECTION_NAME = "caps_curriculum_collection"

def check_technical_mathematics_extraction():
    """
    Specifically checks if Technical Mathematics textbooks were effectively extracted
    from the Chroma DB and provides detailed analysis.
    """
    print("=" * 80)
    print("TECHNICAL MATHEMATICS EXTRACTION ANALYSIS")
    print("=" * 80)
    
    # Initialize embeddings (must match what was used for ingestion)
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=GOOGLE_API_KEY)

    try:
        # Load the existing Chroma vector database
        vectorstore = Chroma(
            persist_directory=CHROMA_DB_DIR,
            embedding_function=embeddings,
            collection_name=COLLECTION_NAME
        )
        
        print(f"✓ Successfully connected to Chroma DB")
        print(f"✓ Total documents in collection: {vectorstore._collection.count()}")
        print()

        # Query for Technical Mathematics documents
        tech_math_results = vectorstore._collection.get(
            where={"subject": "Technical Mathematics"},
            include=['metadatas', 'documents']
        )
        
        metadatas = tech_math_results.get('metadatas', [])
        documents = tech_math_results.get('documents', [])
        
        if not metadatas:
            print("❌ NO TECHNICAL MATHEMATICS DOCUMENTS FOUND!")
            print("\nPossible reasons:")
            print("1. No Technical Mathematics files were placed in curriculum_docs folder")
            print("2. Files don't follow naming convention (should be like 'Textbook_TechnicalMathematics_Gr10_TopicName.pdf')")
            print("3. Subject name mapping issue in RAG ingestion")
            
            # Let's check what subjects ARE in the database
            print("\n" + "="*50)
            print("CHECKING ALL SUBJECTS IN DATABASE:")
            print("="*50)
            all_results = vectorstore._collection.get(include=['metadatas'])
            all_metadatas = all_results.get('metadatas', [])
            
            subjects = set()
            for md in all_metadatas:
                if 'subject' in md:
                    subjects.add(md['subject'])
            
            print("Found subjects:")
            for subject in sorted(subjects):
                print(f"  - {subject}")
            
            return

        print(f"✓ Found {len(metadatas)} Technical Mathematics document chunks")
        print()

        # Analyze by grade and document type
        grade_analysis = defaultdict(lambda: defaultdict(int))
        topic_analysis = defaultdict(set)
        doc_type_analysis = defaultdict(int)
        source_files = set()
        
        for md in metadatas:
            grade = md.get('grade', 'Unknown')
            doc_type = md.get('document_type', 'Unknown')
            topic = md.get('topic', 'No Topic')
            source_file = md.get('source_filename', 'Unknown')
            
            grade_analysis[grade][doc_type] += 1
            topic_analysis[grade].add(topic)
            doc_type_analysis[doc_type] += 1
            source_files.add(source_file)

        # Display grade breakdown
        print("📊 GRADE AND DOCUMENT TYPE BREAKDOWN:")
        print("-" * 50)
        grade_table = []
        for grade in sorted(grade_analysis.keys(), key=lambda x: int(x) if x.isdigit() else 999):
            for doc_type, count in grade_analysis[grade].items():
                grade_table.append([f"Grade {grade}", doc_type, count])
        
        if grade_table:
            print(tabulate(grade_table, headers=["Grade", "Document Type", "Chunks"], tablefmt="grid"))
        
        print(f"\n📚 TOTAL SOURCE FILES: {len(source_files)}")
        print("Source files found:")
        for file in sorted(source_files):
            print(f"  - {file}")

        # Display topics by grade
        print(f"\n📋 TOPICS BY GRADE:")
        print("-" * 50)
        for grade in sorted(topic_analysis.keys(), key=lambda x: int(x) if x.isdigit() else 999):
            topics = topic_analysis[grade]
            print(f"\nGrade {grade} ({len(topics)} topics):")
            for topic in sorted(topics):
                if topic != 'No Topic':
                    print(f"  ✓ {topic}")
                else:
                    print(f"  ⚠️  {topic}")

        # Sample content analysis
        print(f"\n📄 SAMPLE CONTENT ANALYSIS:")
        print("-" * 50)
        
        # Show sample content from each grade
        for grade in sorted(set(md.get('grade') for md in metadatas), key=lambda x: int(x) if x.isdigit() else 999):
            grade_docs = [(md, doc) for md, doc in zip(metadatas, documents) if md.get('grade') == grade]
            if grade_docs:
                sample_md, sample_doc = grade_docs[0]
                print(f"\nGrade {grade} sample content:")
                print(f"Topic: {sample_md.get('topic', 'N/A')}")
                print(f"Source: {sample_md.get('source_filename', 'N/A')}")
                print(f"Content preview (first 200 chars):")
                print(f"  {sample_doc[:200]}...")
                
                # Check content quality
                content_length = len(sample_doc.strip())
                if content_length < 50:
                    print(f"  ⚠️  Warning: Content seems very short ({content_length} chars)")
                elif content_length > 500:
                    print(f"  ✓ Good content length ({content_length} chars)")
                else:
                    print(f"  ~ Moderate content length ({content_length} chars)")

        # Quality assessment
        print(f"\n🎯 EXTRACTION QUALITY ASSESSMENT:")
        print("-" * 50)
        
        total_chunks = len(metadatas)
        chunks_with_topics = sum(1 for md in metadatas if md.get('topic', '').strip() and md.get('topic') != 'No Topic')
        chunks_with_content = sum(1 for doc in documents if len(doc.strip()) > 100)
        
        print(f"Total chunks: {total_chunks}")
        print(f"Chunks with topics: {chunks_with_topics} ({chunks_with_topics/total_chunks*100:.1f}%)")
        print(f"Chunks with substantial content (>100 chars): {chunks_with_content} ({chunks_with_content/total_chunks*100:.1f}%)")
        
        # Overall assessment
        if chunks_with_topics / total_chunks > 0.8 and chunks_with_content / total_chunks > 0.9:
            print("\n✅ EXTRACTION QUALITY: EXCELLENT")
            print("Technical Mathematics textbooks appear to be well extracted!")
        elif chunks_with_topics / total_chunks > 0.6 and chunks_with_content / total_chunks > 0.7:
            print("\n🟡 EXTRACTION QUALITY: GOOD")
            print("Technical Mathematics textbooks are mostly well extracted with some minor issues.")
        else:
            print("\n❌ EXTRACTION QUALITY: NEEDS IMPROVEMENT")
            print("There may be issues with topic extraction or content quality.")

        # Check for expected topics (based on curriculum structure)
        expected_topics = {
            "10": ["Advanced Geometry", "Technical Algebra", "Technical Number Systems"],
            "11": ["Advanced Geometry", "Technical Algebra"],
            "12": ["Technical Calculus Studio", "Technical Number Systems"]
        }
        
        print(f"\n🎯 CURRICULUM ALIGNMENT CHECK:")
        print("-" * 50)
        
        for grade, expected in expected_topics.items():
            actual_topics = topic_analysis.get(grade, set())
            print(f"\nGrade {grade}:")
            print(f"Expected topics: {', '.join(expected)}")
            print(f"Found topics: {', '.join(sorted(actual_topics)) if actual_topics else 'None'}")
            
            if actual_topics:
                missing = set(expected) - actual_topics
                extra = actual_topics - set(expected)
                if missing:
                    print(f"  ⚠️  Missing: {', '.join(missing)}")
                if extra:
                    print(f"  ℹ️  Additional: {', '.join(extra)}")
                if not missing and not extra:
                    print(f"  ✅ Perfect match!")
            else:
                print(f"  ❌ No topics found for this grade")

    except Exception as e:
        print(f"❌ Error accessing ChromaDB: {e}")
        print(f"Please ensure your ChromaDB directory '{CHROMA_DB_DIR}' exists and contains data.")

if __name__ == "__main__":
    check_technical_mathematics_extraction()