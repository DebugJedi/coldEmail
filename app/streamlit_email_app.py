import streamlit as st
from emailGenerator import E_generator
from PIL import Image
import streamlit_shadcn_ui as ui
from resume_extract import extract_resume


with open("assets/style.css") as f:
        st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
# Image to display
img = Image.open('app/resources/photos/Email-Generator.jpg')
st.image(img)

# Title
st.write("<span class = 'header email_app'>📧 Email Generator</span>", unsafe_allow_html=True)

# Document upload
doc_file = st.file_uploader("Upload your resume/document",
                            type=["pdf"])

jobPosting = st.text_input("Enter a job URL:", value = "https://boards.greenhouse.io/benchling/jobs/6270990" )

if st.button("submit"):
    
    extractor_func = extract_resume()
    st.spinner(text="uploading...")
    document = extractor_func.load(doc_file)
    st.write(document)
    
    email = E_generator(jobPosting, document)
    generated_email = email.run()
    st.write("<span class = 'ai generated_email'>{}</span>".format(generated_email), unsafe_allow_html=True)





    
    



