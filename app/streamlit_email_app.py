import streamlit as st
from emailGenerator import E_generator
from PIL import Image
import streamlit_shadcn_ui as ui
from resume_extract import extract_resume

st.set_page_config(
        page_title= "Email Generator App",
        page_icon= "📧",
        layout="wide"
    )


# Image to display
img = Image.open('app/resources/photos/Email-Generator.jpg')
com1, com2, com3 = st.columns([1,2,1], gap= 'small', vertical_alignment='center')
with com1:
    pass
with com2:
    # st.markdown("[link](%s):material/link:"% url)   
    st.image(img)
with com3:
    pass

with open("assets/style.css") as f:
        st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

# Title
st.write("<span class = 'header email_app'>📧 Email Generator</span>", unsafe_allow_html=True)

# Document upload
# st.markdown("******")
doc_file = st.file_uploader("Resume/CV (PDF)",
                            type=["pdf"])

jobPosting = st.text_input("Enter a job URL:", value = "https://boards.greenhouse.io/benchling/jobs/6270990" )
try:
    if st.button("submit"):
        
        with st.spinner("wait for it...."):
            extractor_func = extract_resume()
            st.spinner(text="uploading...")
            document = extractor_func.load(doc_file)
            # st.write(document)
            email = E_generator(jobPosting, document)
            generated_email = email.run()
            st.write("<span class = 'ai generated_email'>{}</span>".format(generated_email), unsafe_allow_html=True)
except AttributeError:
     st.write("Please upload a file...")
except:
     st.write("Please fill all the necessary info..")
     




    
    



