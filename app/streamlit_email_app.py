import streamlit as st
from emailGenerator import E_generator
from PIL import Image
import streamlit_shadcn_ui as ui

# trigger_btn = ui.button(text="Trigger Button", key='trigger_btn')

# ui.alert_dialog(
#     show=trigger_btn,
#     title="Alert Dialog",
#     description="This is an alert dialog",
#     confirm_label="OK",
#     cancel_label="Cancel",
#     key="alert_dialog1",

# )


# col1, col2, col3 = st.columns(3)
# with col1:
#     st.write(' ')
# with col2:
with open("assets/style.css") as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
img = Image.open('app/resources/photos/Email-Generator.jpg')
st.image(img)
# with col3:
#     st.write(' ')

st.markdown("<span class = 'header email_app'>📧 Email Generator</span>", unsafe_allow_html=True)
jobPosting = st.text_input("Enter a job URL:", value = "https://boards.greenhouse.io/benchling/jobs/6270990" )
submit_button = st.button("Submit")


if submit_button:

    email = E_generator(jobPosting)
    generated_email = email.run()
    st.write(generated_email)

    
