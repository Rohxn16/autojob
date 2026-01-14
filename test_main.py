from ResumeUploader.document_reader import pdf2String
from ResumeUploader.vectorstore import MilvusManager
from ResumeUploader.embedder import Embedder
from Fetcher.basic_retriever import LLMRecommender

if __name__ == '__main__':
    emb_engine = Embedder()
    resume_text = pdf2String('Resume.pdf')
    manager = MilvusManager()
    manager.reset_collection()
    recommender = LLMRecommender()
    chunks = emb_engine.chunker(resume_text)
    data = []
    for chunk in chunks:
        embedded_chunk = emb_engine.embed_text(chunk)
        data.append({
            'vector':embedded_chunk,
            'text':chunk
        })
    manager.push_to_milvus(data)
    skills = recommender.recommend(resume_text)
    print(skills)