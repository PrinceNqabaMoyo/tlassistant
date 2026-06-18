import os
from dotenv import load_dotenv
import google.generativeai as genai
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma
from tabulate import tabulate # For pretty printing

# Load environment variables from .env file
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Configure Gemini API (needed for embeddings even if just loading Chroma)
genai.configure(api_key=GOOGLE_API_KEY)

# --- Configuration ---
CHROMA_DB_DIR = "chroma_db_langchain"
COLLECTION_NAME = "caps_curriculum_collection"

def diagnose_topics_in_chroma(subject_name, grade):
    """
    Queries ChromaDB for documents matching a specific subject and grade
    and prints their metadata, focusing on topic information.
    """
    print(f"--- Diagnosing documents for Subject: '{subject_name}', Grade: '{grade}' ---")
    
    # Initialize embeddings (must match what was used for ingestion)
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=GOOGLE_API_KEY)

    try:
        # Load the existing Chroma vector database
        vectorstore = Chroma(
            persist_directory=CHROMA_DB_DIR,
            embedding_function=embeddings,
            collection_name=COLLECTION_NAME
        )
        
        # Query ChromaDB for documents with matching subject and grade metadata
        # Note: Chroma's `get` method can filter by metadata.
        # Ensure the subject name matches exactly what's stored (e.g., "Economic and Management Sciences")
        results = vectorstore._collection.get(
            where={
                "$and": [ # NEW: Use $and to combine multiple conditions
                    {"subject": subject_name},
                    {"grade": str(grade)} # Ensure grade is string if stored as such
                ]
            },
            include=['metadatas']
        )
        
        metadatas = results.get('metadatas', [])

        if not metadatas:
            print(f"\nNo documents found in ChromaDB for '{subject_name}' Grade {grade} with the specified metadata.")
            print("This could mean:")
            print("1. No such files were in 'curriculum_docs'.")
            print("2. Filename parsing in 'RAG Ingestion.txt' did not correctly extract subject/grade for these files.")
            print("   - Double check filenames like 'Textbook_EMS_Gr9_Topic.pdf' or 'StudyGuide_EMS_Gr9_Topic.pdf'.")
            print("   - Ensure 'EMS' is correctly mapped to 'Economic and Management Sciences' in parse_filename_for_metadata.")
            return

        print(f"\nFound {len(metadatas)} documents for '{subject_name}' Grade {grade}. Metadata details:")
        
        # Prepare data for tabulate
        table_data = []
        headers = ["Filename", "Doc Type", "Subject", "Grade", "Topic", "Page/Row"]

        for md in metadatas:
            filename = md.get('source_filename', 'N/A')
            doc_type = md.get('document_type', 'N/A')
            subject = md.get('subject', 'N/A')
            grade_val = md.get('grade', 'N/A')
            topic = md.get('topic', 'N/A') # This is what we're looking for
            page_row = md.get('page_number', md.get('row_number', 'N/A'))
            
            table_data.append([filename, doc_type, subject, grade_val, topic, page_row])
        
        print(tabulate(table_data, headers=headers, tablefmt="grid"))
        print("\nIf 'Topic' column is empty or incorrect, the issue is in RAG Ingestion's filename parsing.")
        print("If topics appear correct here, the issue is in build_curriculum_data.txt's processing logic.")

    except Exception as e:
        print(f"\nAn error occurred while querying ChromaDB: {e}")
        print(f"Please ensure your ChromaDB directory '{CHROMA_DB_DIR}' exists and contains data.")

if __name__ == "__main__":
    # Call the function for the problematic subject and grade
    diagnose_topics_in_chroma("Economic and Management Sciences", 9)
    # You can change these parameters to check other subjects/grades if needed
    # diagnose_topics_in_chroma("Accounting", 10)
