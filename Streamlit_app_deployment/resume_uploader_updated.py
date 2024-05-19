import streamlit as st

from io import StringIO
import pdfplumber
import time
import spacy
from spacy.cli import download
download("en_core_web_md")   
nlp = spacy.load("en_core_web_md")
print("changes")

if "skill_set" not in st.session_state.keys():
    skill_set = ["AWS", "Python", "Azure", "Angular"]
    
    st.session_state["skill_set"] = sorted(skill_set)
else:
    skill_set = sorted(st.session_state["skill_set"])
    file = st.session_state['file']

def extract_data(feed):
    data = []
    with pdfplumber.open(feed) as pdf:
        pages = pdf.pages
        for p in pages:
            data.append(p.extract_text())

    verified = set()
    user_name = None
    email_id = None
    for skills in st.session_state["parameters"]:
        for text in data:
            # if str(skills).lower() in text.lower():
            #     verified.append(skills)
            tokenized_data = nlp(text)
        
        for token in tokenized_data:
            if token.ent_type_ == 'PERSON' and user_name is None:
                user_name = token
            if token.like_email:
                email_id = token
            if token.ent_type_ == 'ORG' and str(skills).lower() == str(token).lower():
                verified.add(str(token))

    if len(verified) == 0 or email_id is None:
        return "Profile does not match"
    return f"{user_name} with email id {email_id} has experience in {','.join(verified)}"    


def process_skill_set(file, place_holder):
    for uploaded_file in file:
        stringio = extract_data(uploaded_file)
        progress_text = "Processing your documents"
        my_bar = place_holder.progress(0, text=progress_text)
        for percent_complete in range(100):
            time.sleep(0.01)
            my_bar.progress(percent_complete + 1, text=progress_text)
        place_holder.write(stringio)


def warning(message = "", activate = False):
        st.error(message, icon="🚨")

def layout_loader(skill_set):

        st.title(':blue[Resume Analyzer] :sunglasses:')       

        with st.popover("Additional Skill"):
            additional_skill = st.text_area('Type your skill set', placeholder="IAM") 
            st.session_state['additional_skill'] = additional_skill
            submit_button = st.button("Submit")
            if submit_button:
                skill_set.append(additional_skill)
                st.session_state["skill_set"] = skill_set

        st.session_state["parameters"] = st.multiselect("Select required skill set", sorted(skill_set), placeholder="Python")
        file = st.file_uploader("Upload your Resume in (.pdf format)",accept_multiple_files=True)
        st.session_state['file'] = file

        place_holder = st.empty()
        process_button = st.button("Process")
        if process_button:
            if len(file) == 0:
                warning("Upload the resume!!!")
            if len(st.session_state.get("parameters")) == 0:
                warning("Kindly select the required skill set")
            else:
                process_skill_set(file, place_holder)

        

layout_loader(skill_set=skill_set)