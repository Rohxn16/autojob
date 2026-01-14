"""
Uses the cosine similarity fetch defined in the vectorstore to get us the top 5 contexts, passing that to the LLM we get a structured output fitting our model
"""

from .Model import Model
from ResumeUploader.vectorstore import MilvusManager
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage,SystemMessage

class LLMRecommender:
    def __init__(self):
        self.manager = MilvusManager()
        self.resume_context = self.manager.simple_cosine_sim_fetch('Top skills according to my resume')

    def recommend(self,context):
        llm = ChatOllama(
            model='gemma3:4b',
            temperature=0,
            num_predict=1024,
            num_ctx=2048
        )

        messages = [
            SystemMessage(
                """
                    You are an expert career coach who tells people what job they are best fit for by analyzing their resume and taking into context
                    i. their education
                    ii. technical knowledge
                    iii. projects
                    iv. co curricular activities
                """
            ),
            HumanMessage(
                content=f'Given the context to my resume suggest 3 job roles that would allow me to flourish in carrer {context}.'
            )
        ]

        llm_struct = llm.with_structured_output(Model)
        response = llm_struct.invoke(messages)

        return response.skill1,response.skill2,response.skill3,response.skill4,response.skill5