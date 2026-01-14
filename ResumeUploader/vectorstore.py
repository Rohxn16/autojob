from pymilvus import MilvusClient
from typing import List
from .embedder import Embedder
class MilvusManager:
    
    def __init__(self):
        """
        Module to manage Milvus client context and use it to perform vector operations like fetching and storing data into vectorstore
        """
        self.embedder = Embedder()
        self.uri = "./milvusdemo.db"
        self.collection_name = "sample_collection"
        self.client = MilvusClient(uri=self.uri)
        if(not self.client.has_collection(collection_name=self.collection_name)):
            self.client.create_collection(
                collection_name=self.collection_name,
                dimension=self.embedder.get_dimensions(),
                auto_id=True,
                enable_dynamic_field=True)
    
    def push_to_milvus(self,data:List[dict]):
        """
        Push labelled vectorized data into milvus database
        """
        inserted_data = self.client.insert(collection_name=self.collection_name,data=data)
        if inserted_data:
            print(f"Successfully inserted {len(data)} chunks into Milvus.")
        else:
            print('Error inserting data')

    def simple_cosine_sim_fetch(self, question: str):
        """
        Fetch the top k matches with distances without reraking using naive approach
        """
        vector = self.embedder.embed_text(question)
        search_res = self.client.search(
            collection_name=self.collection_name,
            data=[vector],
            anns_field='vector',
            limit=5,
            search_params={
                'params':{},
                'metric_type':'COSINE'},
            output_fields=['text']
        )
        retrieved_lines_with_distances = [
        (res["entity"]["text"], res["distance"]) for res in search_res[0]
        ]
        return retrieved_lines_with_distances
    
    def reset_collection(self):
        """
        Drops and recreates the collection to start fresh.
        """
        if self.client.has_collection(self.collection_name):
            self.client.drop_collection(self.collection_name)
            print(f"Collection '{self.collection_name}' dropped.")
            
        # Recreate it using the same dimensions
        self.client.create_collection(
            collection_name=self.collection_name,
            dimension=self.embedder.get_dimensions(),
            auto_id=True,
            enable_dynamic_field=True
        )
        print(f"Collection '{self.collection_name}' recreated.")