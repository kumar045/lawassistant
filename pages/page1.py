import streamlit as st
from streamlit_mic_recorder import speech_to_text

st.title("Form with Speech to Text")

class SendRequests:
    def __init__(self):
        self.email = ""
        self.subject = ""
        self.problem_type = None
        self.info = ""
        self.report_file = None
        self.language = "en"

    def display_form(self):
        # Dropdown for language selection
        language_options = {
            "English": "en",
            "Hindi": "hi",
            "Spanish": "es",
            "Punjabi": "pa",
            "Chinese": "zh"
        }
        selected_language = st.selectbox("Select Language", options=list(language_options.keys()), key='language_select')
        language_code = language_options[selected_language]

        # Speech to text for each field
        email_text = speech_to_text(language=language_code, start_prompt='Email 🎙️', use_container_width=True, just_once=True, key='email_stt')
        subject_text = speech_to_text(language=language_code, start_prompt='Subject 🎙️', use_container_width=True, just_once=True, key='subject_stt')
        info_text = speech_to_text(language=language_code, start_prompt='Info 🎙️', use_container_width=True, just_once=True, key='info_stt')

        with st.form(key="request_form"):
            # Form fields with pre-filled speech-to-text data
            self.email = st.text_input("Your email address", value=email_text if email_text else self.email)
            self.subject = st.text_input("Subject", value=subject_text if subject_text else self.subject)
            self.problem_type = st.selectbox(
                "Type of Problem", 
                options=("Report Content", "Legal Inquiries", "Report Copyright Infringement"),
                key='problem_type'
            )
            self.info = st.text_area("Description", value=info_text if info_text else self.info)
            self.report_file = st.file_uploader("Attachment (optional)", key='report_file')
            
            submit_button = st.form_submit_button("Submit")

            if submit_button:
                self.process_request()

    @staticmethod
    def process_request():
        with st.spinner("Sending..."):
            st.success("Request submitted!")

requests = SendRequests()
requests.display_form()
