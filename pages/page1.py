import streamlit as st
from streamlit_mic_recorder import speech_to_text

st.title("Form")

class SendRequests:
    def __init__(self):
        self.email = ""
        self.subject = ""
        self.problem_type = None
        self.info = ""
        self.report_file = None

    def display_form(self):
        # Buttons for speech-to-text outside the form
        if st.button("Speak Email"):
            self.email = speech_to_text(key="email_stt")
        if st.button("Speak Subject"):
            self.subject = speech_to_text(key="subject_stt")
        if st.button("Speak Description"):
            self.info = speech_to_text(key="info_stt")

        with st.form(key="request_form"):
            # Form fields
            self.email = st.text_input("Your email address", value=self.email, key='email')
            self.subject = st.text_input("Subject", value=self.subject, key='subject')
            self.problem_type = st.selectbox(
                "Type of Problem", 
                options=("Report Content", "Legal Inquiries", "Report Copyright Infringement"),
                key='problem_type'
            )
            self.info = st.text_area("Description", value=self.info, key='info')
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
