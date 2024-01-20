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

    def display_form(self):
        with st.form(key="request_form"):
            # Email field with mic button
            col1, col2 = st.columns([3, 1])
            with col1:
                self.email = st.text_input("Your email address", value=self.email, key='email')
            with col2:
                if st.button("🎙️", key="email_mic"):
                    self.email = speech_to_text(language='en', use_container_width=True, key='email_stt')

            # Subject field with mic button
            col1, col2 = st.columns([3, 1])
            with col1:
                self.subject = st.text_input("Subject", value=self.subject, key='subject')
            with col2:
                if st.button("🎙️", key="subject_mic"):
                    self.subject = speech_to_text(language='en', use_container_width=True, key='subject_stt')

            # Problem type selection
            self.problem_type = st.selectbox(
                "Type of Problem", 
                options=("Report Content", "Legal Inquiries", "Report Copyright Infringement"),
                key='problem_type'
            )

            # Description field with mic button
            col1, col2 = st.columns([3, 1])
            with col1:
                self.info = st.text_area("Description", value=self.info, key='info')
            with col2:
                if st.button("🎙️", key="info_mic"):
                    self.info = speech_to_text(language='en', use_container_width=True, key='info_stt')

            # File uploader
            self.report_file = st.file_uploader("Attachment (optional)", key='report_file')
            
            # Submit button
            submit_button = st.form_submit_button("Submit")

            if submit_button:
                self.process_request()

    @staticmethod
    def process_request():
        with st.spinner("Sending..."):
            st.success("Request submitted!")

requests = SendRequests()
requests.display_form()
