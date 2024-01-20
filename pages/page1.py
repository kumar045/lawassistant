import streamlit as st
from streamlit_mic_recorder import stt_button

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
            self.email = st.text_input("Your email address", key='email')
            self.subject = st.text_input("Subject", key='subject')
            self.problem_type = st.selectbox(
                "Type of Problem", 
                options=("Report Content", "Legal Inquiries", "Report Copyright Infringement"),
                key='problem_type'
            )
            self.info = st.text_area("Description", key='info')
            st.caption(
                "Please enter the details of your request. A member of our support staff will respond as soon as possible."
            )
            self.report_file = st.file_uploader("Attachment (optional)", key='report_file')
            
            # Speech to text buttons
            if st.button("Transcribe Email"):
                self.email = stt_button("Speak now", key="stt1")
            if st.button("Transcribe Subject"):
                self.subject = stt_button("Speak now", key="stt2")
            if st.button("Transcribe Description"):
                self.info = stt_button("Speak now", key="stt3")

            submit_button = st.form_submit_button("Submit")

            if submit_button:
                self.process_request()

    @staticmethod
    def process_request():
        with st.spinner("Sending..."):
            st.success("Request submitted!")

requests = SendRequests()
requests.display_form()
