import streamlit as st

def main():
    st.title("Speech Recognition Form")

    # Embed the HTML for speech recognition
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <style>
            .form-field {
                margin: 15px 0;
            }

            label {
                display: block;
                margin-bottom: 5px;
                font-weight: bold;
            }

            input[type="text"], select {
                padding: 10px;
                margin-top: 5px;
                border-radius: 4px;
                border: 1px solid #ddd;
                width: 80%;
            }
        </style>
    </head>
    <body>
        <script>
            const recognition = new webkitSpeechRecognition() || new SpeechRecognition();
            recognition.interimResults = false;
            recognition.continuous = false;

            function startRecognition(inputId) {
                const inputElement = document.getElementById(inputId);
                recognition.start();
                recognition.onresult = event => {
                    const result = event.results[0][0].transcript;
                    inputElement.value = result;
                };
            }
        </script>
    </body>
    </html>
    """
    st.markdown(html_content, unsafe_allow_html=True)

    # Streamlit form for user input
    with st.form(key="request_form"):
        email = st.text_input("Your email address", key="email")
        subject = st.text_input("Subject", key="subject")
        problem_type = st.selectbox(
            "Type of Problem", 
            options=("Report Content", "Legal Inquiries", "Report Copyright Infringement"),
            key="problem_type"
        )
        info = st.text_area("Description", key="info")
        report_file = st.file_uploader("Attachment (optional)", key="report_file")

        # Buttons for activating speech recognition
        st.button("Speak Email", key="speak_email", on_click=lambda: st.markdown(f"<script>startRecognition('email');</script>", unsafe_allow_html=True))
        st.button("Speak Subject", key="speak_subject", on_click=lambda: st.markdown(f"<script>startRecognition('subject');</script>", unsafe_allow_html=True))
        st.button("Speak Description", key="speak_info", on_click=lambda: st.markdown(f"<script>startRecognition('info');</script>", unsafe_allow_html=True))

        submit_button = st.form_submit_button("Submit")

    # Display success message if submitted
    if submit_button:
        st.success("Request submitted!")

if __name__ == "__main__":
    main()
  
