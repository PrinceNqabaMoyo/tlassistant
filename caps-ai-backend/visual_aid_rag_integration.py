"""
Integration script for visual aid descriptions with existing RAG system
"""

import os
import re
from pathlib import Path
from typing import List, Dict, Any
from dotenv import load_dotenv
import google.generativeai as genai
from langchain_community.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document

# Load environment variables
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

class VisualAidRAGIntegration:
    """Integrates visual aid descriptions with existing ChromaDB"""
    
    def __init__(self, chroma_db_path: str = "chroma_db_langchain"):
        self.chroma_db_path = chroma_db_path
        self.embeddings = GoogleGenerativeAIEmbeddings(
            model="models/embedding-001", 
            google_api_key=GOOGLE_API_KEY
        )
    
    def parse_visual_aid_markdown(self, file_path: str) -> Document:
        """Parse a visual aid markdown file into a Document with enhanced metadata"""
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract metadata from the content
        metadata = self._extract_metadata_from_content(content)
        metadata['source_filename'] = os.path.basename(file_path)
        metadata['source_type'] = 'visual_aid_description'
        metadata['document_type'] = 'Visual Aid Description'
        
        return Document(page_content=content, metadata=metadata)
    
    def _extract_metadata_from_content(self, content: str) -> Dict[str, Any]:
        """Extract structured metadata from markdown content"""
        metadata = {}
        
        # Extract title and basic info from header
        title_match = re.search(r'# Visual Aid: (.+?) - (.+?) - Grade (\d+) - (.+)', content)
        if title_match:
            metadata['visual_aid_title'] = title_match.group(1)
            metadata['subject'] = title_match.group(2)
            metadata['grade'] = title_match.group(3)
            metadata['topic'] = title_match.group(4)
        
        # Extract diagram type
        diagram_type_match = re.search(r'Type: (.+)', content)
        if diagram_type_match:
            metadata['diagram_type'] = diagram_type_match.group(1).lower().replace(' ', '_')
        
        # Extract difficulty level
        difficulty_match = re.search(r'Difficulty.*?: (.+)', content)
        if difficulty_match:
            metadata['difficulty_level'] = difficulty_match.group(1).lower()
        
        # Extract learning objectives (count for complexity measure)
        objectives_section = re.search(r'#### Learning Objectives\n(.*?)(?=\n####|\n---|\Z)', content, re.DOTALL)
        if objectives_section:
            objectives = re.findall(r'- (.+)', objectives_section.group(1))
            metadata['learning_objectives_count'] = len(objectives)
            metadata['learning_objectives'] = objectives
        
        # Extract misconceptions addressed
        misconceptions_section = re.search(r'#### Misconceptions Addressed\n(.*?)(?=\n####|\n---|\Z)', content, re.DOTALL)
        if misconceptions_section:
            misconceptions = re.findall(r'- (.+)', misconceptions_section.group(1))
            metadata['addresses_misconceptions'] = len(misconceptions) > 0
            metadata['misconceptions'] = misconceptions
        
        # Extract interactive potential
        interactive_section = re.search(r'#### Animation Opportunities\n(.*?)(?=\n####|\n---|\Z)', content, re.DOTALL)
        animation_section = re.search(r'#### User Interactions\n(.*?)(?=\n####|\n---|\Z)', content, re.DOTALL)
        
        has_interactive = bool(interactive_section or animation_section)
        metadata['has_interactive_potential'] = has_interactive
        
        # Extract search keywords
        keywords_section = re.search(r'#### Search Keywords\n\[(.+?)\]', content)
        if keywords_section:
            keywords = [k.strip() for k in keywords_section.group(1).split(',')]
            metadata['visual_keywords'] = keywords
        
        # Extract related topics
        related_section = re.search(r'#### Related Topics\n\[(.+?)\]', content)
        if related_section:
            related = [t.strip() for t in related_section.group(1).split(',')]
            metadata['related_topics'] = related
        
        return metadata
    
    def ingest_visual_aids_directory(self, visual_aids_dir: str):
        """Ingest all visual aid markdown files from a directory"""
        
        if not os.path.exists(visual_aids_dir):
            print(f"❌ Directory {visual_aids_dir} does not exist")
            return
        
        # Find all markdown files
        md_files = list(Path(visual_aids_dir).glob("**/*.md"))
        
        if not md_files:
            print(f"❌ No markdown files found in {visual_aids_dir}")
            return
        
        print(f"📁 Found {len(md_files)} visual aid files")
        
        # Process each file
        documents = []
        for file_path in md_files:
            try:
                doc = self.parse_visual_aid_markdown(str(file_path))
                documents.append(doc)
                print(f"✅ Processed: {file_path.name}")
            except Exception as e:
                print(f"❌ Error processing {file_path.name}: {e}")
        
        if not documents:
            print("❌ No documents were successfully processed")
            return
        
        # Split documents for better retrieval
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
        )
        chunks = text_splitter.split_documents(documents)
        
        print(f"📄 Split {len(documents)} documents into {len(chunks)} chunks")
        
        # Add to existing ChromaDB
        try:
            # Load existing database
            vectorstore = Chroma(
                persist_directory=self.chroma_db_path,
                embedding_function=self.embeddings,
                collection_name="caps_curriculum_collection"
            )
            
            # Add new chunks
            vectorstore.add_documents(chunks)
            
            print(f"✅ Added {len(chunks)} visual aid chunks to ChromaDB")
            print(f"📊 Total documents in database: {vectorstore._collection.count()}")
            
        except Exception as e:
            print(f"❌ Error adding to ChromaDB: {e}")
    
    def search_visual_aids(self, query: str, subject: str = None, grade: str = None, k: int = 5):
        """Search for visual aids based on query with optional filters"""
        
        try:
            vectorstore = Chroma(
                persist_directory=self.chroma_db_path,
                embedding_function=self.embeddings,
                collection_name="caps_curriculum_collection"
            )
            
            # Build filter
            filter_conditions = [{"document_type": "Visual Aid Description"}]
            
            if subject:
                filter_conditions.append({"subject": subject})
            
            if grade:
                filter_conditions.append({"grade": str(grade)})
            
            filter_dict = {"$and": filter_conditions} if len(filter_conditions) > 1 else filter_conditions[0]
            
            # Search
            results = vectorstore.similarity_search(
                query,
                k=k,
                filter=filter_dict
            )
            
            return results
            
        except Exception as e:
            print(f"❌ Error searching visual aids: {e}")
            return []
    
    def get_visual_aids_by_topic(self, topic: str, subject: str = "Technical Mathematics"):
        """Get all visual aids for a specific topic"""
        
        try:
            vectorstore = Chroma(
                persist_directory=self.chroma_db_path,
                embedding_function=self.embeddings,
                collection_name="caps_curriculum_collection"
            )
            
            results = vectorstore._collection.get(
                where={
                    "$and": [
                        {"document_type": "Visual Aid Description"},
                        {"subject": subject},
                        {"topic": topic}
                    ]
                },
                include=['metadatas', 'documents']
            )
            
            return results
            
        except Exception as e:
            print(f"❌ Error retrieving visual aids by topic: {e}")
            return None

def main():
    """Demonstrate visual aid RAG integration"""
    
    integration = VisualAidRAGIntegration()
    
    print("=" * 80)
    print("VISUAL AID RAG INTEGRATION DEMO")
    print("=" * 80)
    
    # Example: Create a sample visual aids directory structure
    sample_dir = "sample_visual_aids"
    os.makedirs(sample_dir, exist_ok=True)
    
    # Create a sample visual aid file
    sample_content = """# Visual Aid: Pythagorean Theorem Proof - Mathematics - Grade 9 - Geometry

### Metadata
- **ID**: `mathematics_gr9_geometry_geometric_construction_001`
- **Subject**: Mathematics
- **Grade**: 9
- **Topic**: Geometry
- **Diagram Type**: Geometric Construction
- **Difficulty**: Intermediate

#### Visual Description
- Right triangle ABC with legs a=3, b=4, hypotenuse c=5
- Squares constructed on each side showing areas
- Grid background for measurement verification
- Color-coded regions: blue for leg squares, red for hypotenuse square

#### Learning Objectives
- Understand the geometric proof of Pythagorean theorem
- Visualize the relationship between areas of squares
- Connect algebraic and geometric representations

#### Misconceptions Addressed
- Thinking the theorem only works for 3-4-5 triangles
- Confusing perimeter and area relationships
- Not understanding why we square the sides

#### Search Keywords
[pythagorean theorem, right triangle, squares, areas, geometric proof]

#### Related Topics
[Right triangles, Area calculations, Square roots, Coordinate geometry]
"""
    
    sample_file = os.path.join(sample_dir, "pythagorean_proof_gr9.md")
    with open(sample_file, 'w', encoding='utf-8') as f:
        f.write(sample_content)
    
    print(f"📁 Created sample visual aid: {sample_file}")
    
    # Demonstrate ingestion
    print("\n" + "=" * 50)
    print("INGESTING VISUAL AIDS")
    print("=" * 50)
    
    integration.ingest_visual_aids_directory(sample_dir)
    
    # Demonstrate search
    print("\n" + "=" * 50)
    print("SEARCHING VISUAL AIDS")
    print("=" * 50)
    
    results = integration.search_visual_aids("pythagorean theorem proof", subject="Mathematics")
    
    print(f"Found {len(results)} visual aids for 'pythagorean theorem proof':")
    for i, result in enumerate(results, 1):
        print(f"\n{i}. {result.metadata.get('visual_aid_title', 'Unknown Title')}")
        print(f"   Subject: {result.metadata.get('subject', 'N/A')}")
        print(f"   Grade: {result.metadata.get('grade', 'N/A')}")
        print(f"   Topic: {result.metadata.get('topic', 'N/A')}")
        print(f"   Preview: {result.page_content[:200]}...")
    
    # Cleanup
    import shutil
    shutil.rmtree(sample_dir)
    print(f"\n🧹 Cleaned up sample directory: {sample_dir}")

if __name__ == "__main__":
    main()