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

def analyze_topic_organization():
    """
    Analyzes how chunks are organized by topic and demonstrates
    how to access chunks for specific topics.
    """
    print("=" * 80)
    print("TECHNICAL MATHEMATICS TOPIC ORGANIZATION ANALYSIS")
    print("=" * 80)
    
    # Initialize embeddings
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=GOOGLE_API_KEY)

    try:
        # Load the existing Chroma vector database
        vectorstore = Chroma(
            persist_directory=CHROMA_DB_DIR,
            embedding_function=embeddings,
            collection_name=COLLECTION_NAME
        )
        
        # Query for Technical Mathematics documents
        tech_math_results = vectorstore._collection.get(
            where={"subject": "Technical Mathematics"},
            include=['metadatas', 'documents']
        )
        
        metadatas = tech_math_results.get('metadatas', [])
        documents = tech_math_results.get('documents', [])
        
        print(f"Total Technical Mathematics chunks: {len(metadatas)}")
        print()

        # Analyze topic distribution
        topic_analysis = defaultdict(lambda: {"count": 0, "grades": set(), "doc_types": set(), "files": set()})
        chunks_without_topics = 0
        
        for md in metadatas:
            topic = md.get('topic', '').strip()
            grade = md.get('grade', 'Unknown')
            doc_type = md.get('document_type', 'Unknown')
            source_file = md.get('source_filename', 'Unknown')
            
            if not topic or topic == 'No Topic':
                chunks_without_topics += 1
                topic = "NO_TOPIC_METADATA"
            
            topic_analysis[topic]["count"] += 1
            topic_analysis[topic]["grades"].add(grade)
            topic_analysis[topic]["doc_types"].add(doc_type)
            topic_analysis[topic]["files"].add(source_file)

        print("📊 TOPIC METADATA ANALYSIS:")
        print("-" * 60)
        print(f"Chunks WITH topic metadata: {len(metadatas) - chunks_without_topics}")
        print(f"Chunks WITHOUT topic metadata: {chunks_without_topics}")
        print(f"Topic metadata completeness: {((len(metadatas) - chunks_without_topics) / len(metadatas) * 100):.1f}%")
        print()

        # Display topic distribution table
        print("📋 TOPICS AND CHUNK DISTRIBUTION:")
        print("-" * 60)
        
        topic_table = []
        for topic, data in sorted(topic_analysis.items(), key=lambda x: x[1]["count"], reverse=True):
            if topic != "NO_TOPIC_METADATA":
                grades_str = ", ".join(sorted(data["grades"]))
                topic_table.append([
                    topic[:40] + "..." if len(topic) > 40 else topic,
                    data["count"],
                    grades_str,
                    len(data["files"])
                ])
        
        if topic_table:
            print(tabulate(topic_table, 
                         headers=["Topic", "Chunks", "Grades", "Files"], 
                         tablefmt="grid"))
        
        # Show why some chunks don't have topics
        print(f"\n⚠️  CHUNKS WITHOUT TOPIC METADATA ({chunks_without_topics} chunks):")
        print("-" * 60)
        no_topic_analysis = defaultdict(int)
        for md in metadatas:
            topic = md.get('topic', '').strip()
            if not topic or topic == 'No Topic':
                doc_type = md.get('document_type', 'Unknown')
                no_topic_analysis[doc_type] += 1
        
        for doc_type, count in sorted(no_topic_analysis.items(), key=lambda x: x[1], reverse=True):
            print(f"  {doc_type}: {count} chunks")
        
        print("\nℹ️  Note: Exam papers and syllabi typically don't have specific topic metadata")
        print("   because they cover multiple topics or are general curriculum documents.")

        return topic_analysis, metadatas, documents

    except Exception as e:
        print(f"❌ Error accessing ChromaDB: {e}")
        return None, None, None

def demonstrate_topic_access(topic_analysis, metadatas, documents):
    """
    Demonstrates how to access chunks for specific topics
    """
    if not topic_analysis:
        return
    
    print("\n" + "=" * 80)
    print("HOW TO ACCESS CHUNKS BY TOPIC")
    print("=" * 80)
    
    # Filter out NO_TOPIC_METADATA for this demo
    available_topics = [topic for topic in topic_analysis.keys() if topic != "NO_TOPIC_METADATA"]
    
    print("📋 AVAILABLE TOPICS FOR SEARCH:")
    print("-" * 40)
    for i, topic in enumerate(sorted(available_topics)[:10], 1):
        count = topic_analysis[topic]["count"]
        grades = ", ".join(sorted(topic_analysis[topic]["grades"]))
        print(f"{i:2d}. {topic} ({count} chunks, Grades: {grades})")
    
    if len(available_topics) > 10:
        print(f"    ... and {len(available_topics) - 10} more topics")
    
    # Demonstrate accessing a specific topic
    if available_topics:
        demo_topic = available_topics[0]  # Use the first available topic
        print(f"\n🔍 DEMONSTRATION: Accessing chunks for '{demo_topic}'")
        print("-" * 60)
        
        topic_chunks = []
        for i, md in enumerate(metadatas):
            if md.get('topic', '').strip() == demo_topic:
                topic_chunks.append({
                    'index': i,
                    'metadata': md,
                    'content': documents[i]
                })
        
        print(f"Found {len(topic_chunks)} chunks for '{demo_topic}'")
        
        # Show first few chunks as examples
        for i, chunk in enumerate(topic_chunks[:3]):
            md = chunk['metadata']
            content = chunk['content']
            
            print(f"\n--- Chunk {i+1} ---")
            print(f"Source: {md.get('source_filename', 'N/A')}")
            print(f"Grade: {md.get('grade', 'N/A')}")
            print(f"Document Type: {md.get('document_type', 'N/A')}")
            print(f"Page/Row: {md.get('page_number', md.get('row_number', 'N/A'))}")
            print(f"Content Preview: {content[:200]}...")
            
        if len(topic_chunks) > 3:
            print(f"\n... and {len(topic_chunks) - 3} more chunks for this topic")

def show_programmatic_access():
    """
    Shows how to programmatically access chunks by topic in your application
    """
    print("\n" + "=" * 80)
    print("PROGRAMMATIC ACCESS PATTERNS")
    print("=" * 80)
    
    code_examples = [
        {
            "title": "1. Search by Specific Topic",
            "code": '''
# Access chunks for a specific topic
def get_chunks_by_topic(vectorstore, topic_name, grade=None):
    where_clause = {
        "$and": [
            {"subject": "Technical Mathematics"},
            {"topic": topic_name}
        ]
    }
    
    # Optionally filter by grade
    if grade:
        where_clause["$and"].append({"grade": str(grade)})
    
    results = vectorstore._collection.get(
        where=where_clause,
        include=['metadatas', 'documents']
    )
    return results

# Example usage:
trigonometry_chunks = get_chunks_by_topic(vectorstore, "Trigonometry", grade="10")
'''
        },
        {
            "title": "2. Semantic Search within Topic",
            "code": '''
# Combine topic filtering with semantic search
def semantic_search_in_topic(vectorstore, query, topic_name, k=5):
    # First filter by topic
    topic_filter = {
        "$and": [
            {"subject": "Technical Mathematics"},
            {"topic": topic_name}
        ]
    }
    
    # Then do semantic search within those chunks
    results = vectorstore.similarity_search(
        query, 
        k=k,
        filter=topic_filter
    )
    return results

# Example usage:
calculus_derivatives = semantic_search_in_topic(
    vectorstore, 
    "how to find derivatives of polynomial functions",
    "Differentiation"
)
'''
        },
        {
            "title": "3. Get All Topics for a Grade",
            "code": '''
# Get all available topics for a specific grade
def get_topics_by_grade(vectorstore, grade):
    results = vectorstore._collection.get(
        where={
            "$and": [
                {"subject": "Technical Mathematics"},
                {"grade": str(grade)}
            ]
        },
        include=['metadatas']
    )
    
    topics = set()
    for metadata in results.get('metadatas', []):
        topic = metadata.get('topic', '').strip()
        if topic and topic != 'No Topic':
            topics.add(topic)
    
    return sorted(list(topics))

# Example usage:
grade_12_topics = get_topics_by_grade(vectorstore, "12")
print("Grade 12 Topics:", grade_12_topics)
'''
        }
    ]
    
    for example in code_examples:
        print(f"\n{example['title']}:")
        print("-" * 50)
        print(example['code'])

if __name__ == "__main__":
    topic_analysis, metadatas, documents = analyze_topic_organization()
    if topic_analysis:
        demonstrate_topic_access(topic_analysis, metadatas, documents)
        show_programmatic_access()
        
        print("\n" + "=" * 80)
        print("SUMMARY")
        print("=" * 80)
        print("✅ YES - Chunks ARE organized by topic metadata")
        print("✅ YES - You CAN access chunks for specific topics")
        print("⚠️  LIMITATION - Some chunks (exams/syllabi) lack topic metadata")
        print("💡 SOLUTION - Use combination of topic filtering + semantic search")
        print("             for best results in your RAG application")