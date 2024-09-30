import streamlit as st
from emailGenerator import E_generator
from PIL import Image
import streamlit_shadcn_ui as ui
from resume_extract import extract_resume

# Image to display
img = Image.open('app/resources/photos/Email-Generator.jpg')
st.image(img)

# Title
st.write("<span class = 'header email_app'>📧 Email Generator</span>", unsafe_allow_html=True)

# Document upload
doc_file = st.file_uploader("Upload your resume/document",
                            type=["pdf"])
if st.button("Upload"):
    extractor_func = extract_resume(doc_file)

jobPosting = st.text_input("Enter a job URL:", value = "https://boards.greenhouse.io/benchling/jobs/6270990" )

submit_button = st.button("Submit")
with open("assets/style.css") as f:
        st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
try:
    if submit_button:
        
        email = E_generator(jobPosting, extractor_func)
        generated_email = email.run()
        st.write("<span class = 'ai generated_email'>{}</span>".format(generated_email), unsafe_allow_html=True)
except:
     print("Please upload a document..")     
