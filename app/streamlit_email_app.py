import streamlit as st
from emailGenerator import E_generator
from PIL import Image
import streamlit_shadcn_ui as ui


with open("assets/style.css") as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
img = Image.open('app/resources/photos/Email-Generator.jpg')
st.image(img)


st.write("<span class = 'header email_app'>📧 Email Generator</span>", unsafe_allow_html=True)
jobPosting = st.text_input("Enter a job URL:", value = "https://boards.greenhouse.io/benchling/jobs/6270990" )
submit_button = st.button("Submit")


if submit_button:

    email = E_generator(jobPosting)
    generated_email = email.run()
    st.write("<span class = 'ai generated_email'>{}</span>".format(generated_email), unsafe_allow_html=True)

    
