import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

print("="*50)
print("ENVIRONMENT CHECK")
print("="*50)
print(f"GOOGLE_API_KEY exists: {bool(GOOGLE_API_KEY)}")
print(f"GOOGLE_API_KEY length: {len(GOOGLE_API_KEY) if GOOGLE_API_KEY else 0}")

# Check if ChromaDB directory exists
CHROMA_DB_DIR = "chroma_db_langchain"
print(f"ChromaDB directory exists: {os.path.exists(CHROMA_DB_DIR)}")

if os.path.exists(CHROMA_DB_DIR):
    contents = os.listdir(CHROMA_DB_DIR)
    print(f"ChromaDB contents: {contents}")

try:
    import google.generativeai as genai
    print("✓ google.generativeai imported successfully")
except ImportError as e:
    print(f"❌ Failed to import google.generativeai: {e}")

try:
    from langchain_google_genai import GoogleGenerativeAIEmbeddings
    print("✓ GoogleGenerativeAIEmbeddings imported successfully")
except ImportError as e:
    print(f"❌ Failed to import GoogleGenerativeAIEmbeddings: {e}")

try:
    from langchain_chroma import Chroma
    print("✓ Chroma imported successfully")
except ImportError as e:
    print(f"❌ Failed to import Chroma: {e}")

if GOOGLE_API_KEY:
    try:
        import google.generativeai as genai
        genai.configure(api_key=GOOGLE_API_KEY)
        print("✓ Gemini API configured successfully")
    except Exception as e:
        print(f"❌ Failed to configure Gemini API: {e}")

print("\n" + "="*50)
print("QUICK TECHNICAL MATHEMATICS CHECK")
print("="*50)

# Count Technical Mathematics files
curriculum_docs = "curriculum_docs"
if os.path.exists(curriculum_docs):
    all_files = os.listdir(curriculum_docs)
    tech_math_files = [f for f in all_files if "TechnicalMathematics" in f]
    print(f"Total files in curriculum_docs: {len(all_files)}")
    print(f"Technical Mathematics files found: {len(tech_math_files)}")
    
    print("\nTechnical Mathematics files:")
    for i, file in enumerate(tech_math_files[:10]):  # Show first 10
        print(f"  {i+1}. {file}")
    if len(tech_math_files) > 10:
        print(f"  ... and {len(tech_math_files) - 10} more files")
else:
    print("❌ curriculum_docs directory not found")