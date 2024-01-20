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
            # Speech to text buttons for each field
            email_stt = speech_to_text(language='en', use_container_width=True, just_once=True, key='email_stt')
            print(email_stt)
            self.email = st.text_input("Your email address", value=email_stt if email_stt else self.email)

            subject_stt = speech_to_text(language='en', use_container_width=True, just_once=True, key='subject_stt')
            self.subject = st.text_input("Subject", value=subject_stt if subject_stt else self.subject)

            self.problem_type = st.selectbox(
                "Type of Problem", 
                options=("Report Content", "Legal Inquiries", "Report Copyright Infringement"),
                key='problem_type'
            )

            info_stt = speech_to_text(language='en', use_container_width=True, just_once=True, key='info_stt')
            self.info = st.text_area("Description", value=info_stt if info_stt else self.info)

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
