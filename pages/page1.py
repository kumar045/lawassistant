from time import sleep
import streamlit as st
from streamlit_mic_recorder import speech_to_text

st.title("Form")

class SendRequests:
    def __init__(self):
        self.email = None
        self.subject = None
        self.problem_type = None
        self.info = None
        self.report_file = None

    def display_form(self):
        with st.form(key="request_form"):
            self.email = st.text_input("Your email address", value=speech_to_text(key='email_stt'))
            self.subject = st.text_input("Subject", value=speech_to_text(key='subject_stt'))
            self.problem_type = st.selectbox(
                "Type of Problem", options=("Report Content", "Legal Inquiries", "Report Copyright Infringement")
            )
            self.info = st.text_area("Description", value=speech_to_text(key='info_stt'))
            st.caption(
                "Please enter the details of your request. A member of our support staff will respond as soon as possible."
            )
            self.report_file = st.file_uploader("Attachment (optional)")
            submit_button = st.form_submit_button("Submit")

            if submit_button:
                self.process_request()

    @staticmethod
    def process_request():
        with st.spinner("Sending..."):
            sleep(10)
            st.success("Request submitted!")

requests = SendRequests()
requests.display_form()
