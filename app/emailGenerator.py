from langchain_groq import ChatGroq
import streamlit as st
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
# import chromadb
from langchain_community.document_loaders import PyPDFLoader
from jobPosting import extract_jobinfo
from myData import my_data
from resume_extract import extract_resume
from dotenv import load_dotenv
import yaml


print()
ignore = st.secrets['ignore']
comp_ignore = st.secrets['comp_ignore']
POST = st.secrets['post_url']
class E_generator():
    def __init__(self, POST, file):
        self.file = file
        self.post = POST
        self.llm = ChatGroq(
            model_name= "llama-3.1-70b-versatile",
            temperature=0,
            groq_api_key=st.secrets["groq_api_key"]
        )
    

    def main(self):
        jobpost = extract_jobinfo(self.post)
        job_extract = jobpost.jobPosting()
        # mydata = my_data()
        # my_extract = mydata.load_data()
        # resume = extract_resume()

        resume_extract = self.file
        
        return job_extract, resume_extract
    
    def email(self, resume, page_data):

        page_data,  resume = self.main()
        

        prompt_extract = PromptTemplate.from_template(
            """
            ## Scrapped text from resume:
            from my resume {resume}
            ## INSTRUCTION:
            Scraped is the data which it a bit about my career experince,
            and the resume.
            my name is xyz, I am currently in boston. review the job
            information in {page_data}, and draft me an cold email to be the hiring 
            manger for that job. And donot mention my email and other contact details.
            Never mention the name {ignore} and {comp_ignore}
        """
        )
        chain_extract = prompt_extract | self.llm
        generatedEmail = chain_extract.invoke(input={'page_data': page_data, 'my_data': my_data, 
                                                    'resume':resume,
                                                    'ignore': ignore,
                                                    'comp_ignore': comp_ignore})

        return generatedEmail.content

    def run(self):
       
        job, resume = self.main()
        generated_email = self.email(resume, job)

        return generated_email