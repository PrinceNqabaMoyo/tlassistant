import os
import json
from typing import Dict, List, Any
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings

class CurriculumService:
    def __init__(self):
        self.chroma_db_dir = os.getenv('CHROMA_DB_DIR', 'chroma_db_langchain')
        self.embeddings = GoogleGenerativeAIEmbeddings(
            model="models/embedding-001",
            google_api_key=os.getenv('GOOGLE_API_KEY')
        )
        self.vectorstore = None
        self._initialize_vectorstore()
    
    def _initialize_vectorstore(self):
        """Initialize ChromaDB vectorstore"""
        try:
            self.vectorstore = Chroma(
                persist_directory=self.chroma_db_dir,
                embedding_function=self.embeddings
            )
            print("ChromaDB vectorstore initialized successfully")
        except Exception as e:
            print(f"Error initializing ChromaDB: {e}")
            self.vectorstore = None
    
    def get_curriculum_data(self) -> Dict[str, Any]:
        """Get all curriculum data from ChromaDB"""
        if not self.vectorstore:
            return self._get_fallback_curriculum_data()
        
        try:
            # Get all documents from ChromaDB
            all_docs = self.vectorstore._collection.get(include=['metadatas'])
            
            # Process metadata to create curriculum structure
            curriculum_data = self._process_curriculum_metadata(all_docs['metadatas'])
            
            return curriculum_data
        except Exception as e:
            print(f"Error getting curriculum data: {e}")
            return self._get_fallback_curriculum_data()
    
    def get_topics_by_subject_grade(self, subject: str, grade: str) -> List[Dict[str, Any]]:
        """Get topics for specific subject and grade"""
        if not self.vectorstore:
            return []
        
        try:
            # Query ChromaDB for specific subject and grade
            query = f"subject:{subject} grade:{grade}"
            results = self.vectorstore.similarity_search(query, k=50)
            
            topics = []
            for doc in results:
                if hasattr(doc, 'metadata'):
                    metadata = doc.metadata
                    if metadata.get('subject', '').lower() == subject.lower() and \
                       metadata.get('grade', '').lower() == grade.lower():
                        topics.append({
                            'topic': metadata.get('topic', ''),
                            'description': metadata.get('description', ''),
                            'difficulty': metadata.get('difficulty', ''),
                            'estimated_hours': metadata.get('estimated_hours', 0)
                        })
            
            return topics
        except Exception as e:
            print(f"Error getting topics: {e}")
            return []
    
    def search_curriculum(self, query: str, filters: Dict[str, Any] = None) -> List[Dict[str, Any]]:
        """Search curriculum content"""
        if not self.vectorstore:
            return []
        
        try:
            # Apply filters to query
            search_query = query
            if filters:
                for key, value in filters.items():
                    search_query += f" {key}:{value}"
            
            # Search ChromaDB
            results = self.vectorstore.similarity_search(search_query, k=20)
            
            search_results = []
            for doc in results:
                if hasattr(doc, 'metadata'):
                    metadata = doc.metadata
                    search_results.append({
                        'content': doc.page_content,
                        'subject': metadata.get('subject', ''),
                        'grade': metadata.get('grade', ''),
                        'topic': metadata.get('topic', ''),
                        'relevance_score': metadata.get('relevance_score', 0)
                    })
            
            return search_results
        except Exception as e:
            print(f"Error searching curriculum: {e}")
            return []
    
    def _process_curriculum_metadata(self, metadatas: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Process ChromaDB metadata into curriculum structure"""
        curriculum_data = {
            'mathematics': {},
            'mathematical_literacy': {},
            'technical_mathematics': {}
        }
        
        for metadata in metadatas:
            subject = metadata.get('subject', '').lower()
            grade = metadata.get('grade', '')
            topic = metadata.get('topic', '')
            
            if subject and grade and topic:
                if subject not in curriculum_data:
                    curriculum_data[subject] = {}
                
                if grade not in curriculum_data[subject]:
                    curriculum_data[subject][grade] = []
                
                topic_data = {
                    'name': topic,
                    'description': metadata.get('description', ''),
                    'difficulty': metadata.get('difficulty', ''),
                    'estimated_hours': metadata.get('estimated_hours', 0)
                }
                
                curriculum_data[subject][grade].append(topic_data)
        
        return curriculum_data
    
    def _get_fallback_curriculum_data(self) -> Dict[str, Any]:
        """Fallback curriculum data when ChromaDB is not available"""
        return {
            'mathematics': {
                'grade_7': [
                    {'name': 'Numbers and Operations', 'description': 'Basic number operations', 'difficulty': 'beginner', 'estimated_hours': 2},
                    {'name': 'Algebra', 'description': 'Introduction to algebra', 'difficulty': 'beginner', 'estimated_hours': 3}
                ],
                'grade_8': [
                    {'name': 'Linear Equations', 'description': 'Solving linear equations', 'difficulty': 'intermediate', 'estimated_hours': 4},
                    {'name': 'Geometry', 'description': 'Basic geometric concepts', 'difficulty': 'intermediate', 'estimated_hours': 3}
                ]
            },
            'mathematical_literacy': {
                'grade_10': [
                    {'name': 'Financial Mathematics', 'description': 'Basic financial calculations', 'difficulty': 'beginner', 'estimated_hours': 2},
                    {'name': 'Data Handling', 'description': 'Basic statistics and data', 'difficulty': 'beginner', 'estimated_hours': 3}
                ]
            }
        }
