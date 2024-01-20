import streamlit as st
from streamlit_mic_recorder import stt_button

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
            # Speech to text for each field using stt_button
            self.email = stt_button(key='email_stt', label="Your email address", value=self.email, language='en', type='text')
            self.subject = stt_button(key='subject_stt', label="Subject", value=self.subject, language='en', type='text')
            self.problem_type = st.selectbox(
                "Type of Problem", 
                options=("Report Content", "Legal Inquiries", "Report Copyright Infringement"),
                key='problem_type'
            )
            self.info = stt_button(key='info_stt', label="Description", value=self.info, language='en', type='textarea')
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
