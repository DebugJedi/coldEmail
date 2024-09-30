from langchain_groq import ChatGroq
import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
import yaml


resume_file  = st.secrets['resume']

class extract_resume():
        # https://boards.greenhouse.io/benchling/jobs/6270990
        def __init__(self, file = resume_file):
                self.llm = ChatGroq(
                        model_name= "llama-3.1-70b-versatile",
                        temperature=0,
                        groq_api_key=st.secrets["groq_api_key"]  
                )
                self.file = file

        def load(self):

                loader = PyPDFLoader(self.file)
                resume  = loader.load_and_split()
                # print(res.content)
                
                return resume
        
        

