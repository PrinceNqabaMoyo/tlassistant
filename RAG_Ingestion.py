import os
import re
from dotenv import load_dotenv
import google.generativeai as genai
from langchain_community.document_loaders import PyPDFLoader # RE-ADDED: Import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import pandas as pd
import pdfplumber
from tabulate import tabulate

# Load environment variables from .env file
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Configure Gemini API
genai.configure(api_key=GOOGLE_API_KEY)

# --- Configuration ---
# Directory where all your curriculum documents (PDFs and CSVs) are saved.
DOCS_DIR = "curriculum_docs" 
# Directory to save your vector database.
CHROMA_DB_DIR = "chroma_db_langchain"

# Create directories if they don't exist
os.makedirs(DOCS_DIR, exist_ok=True)
os.makedirs(CHROMA_DB_DIR, exist_ok=True)

def parse_filename_for_metadata(filename: str) -> dict:
    """
    Parses a filename based on the new, detailed naming conventions to extract structured metadata.
    Handles four patterns: Syllabus, Textbook, Exam, and StudyGuide.
    It now extracts the 'topic' directly from Textbook and StudyGuide filenames.
    Updated: Syllabus now extracts a single 'grade' instead of 'grade_range'.
    Updated: Exam regex improved further for flexibility in subject and exam code,
             including specific handling for Physical Sciences sub-types (Chem/Phys).
    Updated: Textbook and StudyGuide topic regex to handle spaces and hyphens,
             and ensure consistent space rendering.
    Added: Debug print for filename parsing.
    """
    metadata = {'source_filename': filename}
    base_name = filename.rsplit('.', 1)[0] # Remove file extension

    # Helper to clean up subject names
    def clean_subject_name(name):
        replacements = {
            'MathematicalLiteracy': 'Mathematical Literacy',
            'TechnicalMathematics': 'Technical Mathematics',
            'PhysicalSciences': 'Physical Sciences',
            'BusinessStudies': 'Business Studies',
            'EMS': 'Economic and Management Sciences',
            'Accounting': 'Accounting'
        }
        for abbr, full_name in replacements.items():
            name = name.replace(abbr, full_name)
        return name.replace('_', ' ')

    # Pattern 1: Syllabus Files (e.g., "Syllabus_BusinessStudies_Gr10.pdf")
    syllabus_pattern = r"Syllabus_([a-zA-Z]+)_Gr(\d+)\.pdf$"
    syllabus_match = re.match(syllabus_pattern, filename)
    if syllabus_match:
        metadata['document_type'] = 'Syllabus'
        metadata['subject'] = clean_subject_name(syllabus_match.group(1))
        metadata['grade'] = syllabus_match.group(2)
        return metadata

    # Pattern 2: Textbook Chapter Files (e.g., "Textbook_Mathematics_Gr7_Algebraic-Expressions.pdf")
    textbook_pattern = r"Textbook_([a-zA-Z]+)_Gr(\d+)_([a-zA-Z0-9\s-]+)\.pdf$"
    textbook_match = re.match(textbook_pattern, filename)
    if textbook_match:
        metadata['document_type'] = 'Textbook Chapter'
        metadata['subject'] = clean_subject_name(textbook_match.group(1))
        metadata['grade'] = textbook_match.group(2)
        metadata['topic'] = textbook_match.group(3).replace('-', ' ')
        return metadata

    # Pattern 3: Exam Files (e.g., "Gr7_Mathematics_Exam_Paper1.pdf", "Gr10_Accounting_Exam1.pdf", "Gr11_PhysicalSciences_Chem_Exam2.pdf")
    exam_pattern = r"Gr(\d+)_([a-zA-Z_]+)(?:_(Chem|Phys))?_Exam_?([a-zA-Z0-9_.-]+)\.pdf$"
    exam_match = re.match(exam_pattern, filename)
    if exam_match:
        metadata['document_type'] = 'Exam Paper'
        metadata['grade'] = exam_match.group(1)
        metadata['subject'] = clean_subject_name(exam_match.group(2))
        if exam_match.group(3):
            metadata['exam_type'] = exam_match.group(3)
        metadata['exam_code'] = exam_match.group(4)
        return metadata
        
    # Pattern 4: StudyGuide Files (e.g., "StudyGuide_Accounting_Gr10_Financial-Statements.pdf")
    studyguide_pattern = r"StudyGuide_([a-zA-Z]+)_Gr(\d+)_([a-zA-Z0-9\s-]+)\.pdf$"
    studyguide_match = re.match(studyguide_pattern, filename)
    if studyguide_match:
        metadata['document_type'] = 'Study Guide'
        metadata['subject'] = clean_subject_name(studyguide_match.group(1))
        metadata['grade'] = studyguide_match.group(2)
        metadata['topic'] = studyguide_match.group(3).replace('-', ' ')
        return metadata

    print(f"Warning: Filename '{filename}' did not match any known pattern. Using basic metadata.")
    # DEBUG: Print all patterns if a file doesn't match to help diagnose
    # print(f"  Attempted patterns: Syllabus: '{syllabus_pattern}', Textbook: '{textbook_pattern}', Exam: '{exam_pattern}', StudyGuide: '{studyguide_pattern}'")
    return metadata

def ingest_documents(docs_folder_path: str, chroma_db_path: str):
    """
    Ingests PDF and CSV documents from a folder, splits them, creates embeddings,
    and stores them in a Chroma vector database with rich metadata.
    This version uses pdfplumber for better PDF and table extraction,
    and PyPDFLoader to ensure maximum content extraction by storing both versions if available.
    """
    all_documents = []
    print(f"Loading documents from '{docs_folder_path}'...")

    for filename in os.listdir(docs_folder_path):
        filepath = os.path.join(docs_folder_path, filename)
        custom_metadata = parse_filename_for_metadata(filename)
        
        try:
            loaded_docs_content_for_file = [] # Accumulate documents for the current file

            if filename.endswith(".pdf"):
                plumber_docs = []
                pypdf_docs = []

                # --- Attempt with pdfplumber ---
                try:
                    with pdfplumber.open(filepath) as pdf:
                        for i, page in enumerate(pdf.pages):
                            page_text = page.extract_text() or ""
                            tables = page.extract_tables()
                            table_texts = []
                            for table in tables:
                                if table and len(table) > 1 and table[0]:
                                    df = pd.DataFrame(table[1:], columns=table[0])
                                    table_markdown = tabulate(df, headers='keys', tablefmt='pipe')
                                    table_texts.append(f"\n\n--- Table on Page {i+1} ---\n{table_markdown}\n--- End Table ---")
                                elif table and table[0]:
                                    df = pd.DataFrame(columns=table[0])
                                    table_markdown = tabulate(df, headers='keys', tablefmt='pipe')
                                    table_texts.append(f"\n\n--- Table on Page {i+1} ---\n{table_markdown}\n--- End Table ---")

                            full_page_content = page_text + "\n".join(table_texts)
                            
                            if full_page_content.strip():
                                doc = Document(
                                    page_content=full_page_content.strip(),
                                    metadata={**custom_metadata, 'page_number': i + 1, 'source_type': 'pdf_page_plumber'}
                                )
                                plumber_docs.append(doc)
                    if plumber_docs:
                        print(f"  -> pdfplumber extracted {len(plumber_docs)} parts from '{filename}'.")
                    else:
                        print(f"  -> pdfplumber extracted 0 parts from '{filename}'.")
                except Exception as e:
                    print(f"  -> pdfplumber encountered an error for '{filename}': {e}")

                # --- Always attempt with PyPDFLoader ---
                try:
                    loader = PyPDFLoader(filepath)
                    pypdf_raw_docs = loader.load()
                    if pypdf_raw_docs:
                        for i, doc in enumerate(pypdf_raw_docs):
                            doc.metadata = {**custom_metadata, **doc.metadata, 'page_number': i + 1, 'source_type': 'pdf_page_pypdf'}
                            pypdf_docs.append(doc)
                        print(f"  -> PyPDFLoader extracted {len(pypdf_docs)} parts from '{filename}'.")
                    else:
                        print(f"  -> PyPDFLoader extracted 0 parts from '{filename}'.")
                except Exception as e:
                    print(f"  -> PyPDFLoader encountered an error for '{filename}': {e}")

                # --- Combine results from both loaders ---
                if plumber_docs:
                    loaded_docs_content_for_file.extend(plumber_docs)
                
                # Only add PyPDFLoader docs if they are different or if pdfplumber failed to extract anything
                # A simple check: if PyPDFLoader extracted content and it's not identical to plumber's (e.g., different number of pages/chunks), add it.
                # For simplicity, if plumber got something, and pypdf also got something, include both.
                # The RAG retriever will ultimately decide which chunk is more relevant.
                if pypdf_docs:
                    # To avoid exact duplicates if both extract identical raw text (unlikely for complex PDFs)
                    # A more sophisticated check would involve content hashing, but for now, we'll just add if PyPDFLoader found content.
                    loaded_docs_content_for_file.extend(pypdf_docs)
                    
                if not plumber_docs and not pypdf_docs:
                    print(f"  -> Neither pdfplumber nor PyPDFLoader extracted any content from '{filename}'.")
                elif plumber_docs and pypdf_docs:
                     print(f"  -> Combined content from both loaders for '{filename}'. Total parts for file: {len(loaded_docs_content_for_file)}")


            elif filename.endswith(".csv"):
                df = pd.read_csv(filepath, encoding='utf-8')
                for index, row in df.iterrows():
                    row_content = ", ".join([f"{col}: {val}" for col, val in row.items()])
                    if row_content.strip():
                        doc = Document(
                            page_content=row_content.strip(),
                            metadata={**custom_metadata, 'row_number': index + 1, 'source_type': 'csv_row'}
                        )
                        loaded_docs_content_for_file.append(doc)
            
            all_documents.extend(loaded_docs_content_for_file)
            print(f"-> Successfully loaded {len(loaded_docs_content_for_file)} total parts from '{filename}' with metadata: {custom_metadata}")

        except Exception as e:
            print(f"xx Error loading '{filename}': {e}. Skipping this file.")

    if not all_documents:
        print("\n--- ATTENTION ---")
        print("No documents were loaded. Please ensure:")
        print(f"1. Your PDF and CSV files are in the '{DOCS_DIR}' folder.")
        print("2. They follow one of the specified naming conventions.")
        print("3. Poppler is installed and accessible for PDF processing.")
        print("-------------------\n")
        return

    # Split documents into smaller, manageable chunks for better retrieval
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_documents(all_documents)
    print(f"\nSplit {len(all_documents)} documents into {len(chunks)} chunks.")

    # Create embeddings using Gemini's embedding model
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=GOOGLE_API_KEY)

    # Create and persist the Chroma vector database
    print(f"Creating and saving vector database to '{chroma_db_path}'...")
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=chroma_db_path,
        collection_name="caps_curriculum_collection" # Using a more general collection name
    )
    
    print("\nVector database created and saved successfully!")
    print(f"Total chunks in DB: {vectorstore._collection.count()}")

if __name__ == "__main__":
    print("--- CAPS AI Agent: Curriculum Ingestion Script ---")
    print(f"This script will ingest your PDF and CSV documents from the '{DOCS_DIR}' folder.")
    print("Please ensure your files follow the correct naming conventions.")
    
    input("\nPress Enter to start the ingestion process...")
    
    ingest_documents(DOCS_DIR, CHROMA_DB_DIR)
    
    print("\nIngestion complete. The curriculum data is ready for your AI agent.")

