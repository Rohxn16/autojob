from langchain_text_splitters import RecursiveCharacterTextSplitter
from typing import List
from ollama import embeddings

class Embedder:
    def __init__(self) -> None:
        self.embedding_model    =   'nomic-embed-text:latest'
        self.chunk_size         =   1000
        self.chunk_overlap      =   100

    def chunker(self,document:str) -> List[str]:
        """
        Returns chunked array of texts from the original text for better storage in vectorstores
        """
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap
        )
        chunks = splitter.split_text(document)
        return chunks

    def embed_text(self, text:str):
        "Returns a single text embed"
        embedded_text = embeddings(model=self.embedding_model, prompt=text)
        return embedded_text['embedding']

    def get_dimensions(self):
        """
        A simple function that uses a dummy text, calls the embedding function with the current embedding model upon it and gets the dimensions of the vector embeddings
        """
        test_text = "Hello, World"
        embed = self.embed_text(test_text)
        return len(embed)

