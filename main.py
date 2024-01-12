import streamlit as st
from streamlit.components.v1 import html

# JavaScript to integrate voice recognition and send data to Streamlit
voice_input_script = """
<button onclick="startDictation()">Start Dictation</button>
<p id="transcript">Transcript will appear here...</p>

<script>
function startDictation() {
    if (window.hasOwnProperty('webkitSpeechRecognition')) {
        var recognition = new webkitSpeechRecognition();

        recognition.continuous = false;
        recognition.interimResults = false;
        recognition.lang = "en-US";
        recognition.start();

        recognition.onresult = function(e) {
            var transcript = e.results[0][0].transcript.toLowerCase();
            document.getElementById('transcript').innerText = transcript;
            if (transcript.startsWith("email")) {
                var email = transcript.replace("email", "").trim();
                window.parent.postMessage({type: 'streamlit:setEmailValue', value: email}, '*');
            } else if (transcript.startsWith("name")) {
                var name = transcript.replace("name", "").trim();
                window.parent.postMessage({type: 'streamlit:setNameValue', value: name}, '*');
            }
            recognition.stop();
        };

        recognition.onerror = function(e) {
            recognition.stop();
        }
    }
}
</script>
"""

# This script hides the elements used for capturing voice input.
hide_streamlit_style = """
<style>
#hiddenEmailField, #hiddenNameField {
    display: none;
}
</style>
"""

def main():
    st.title("Voice Recognition Form")
    html(voice_input_script)
    html(hide_streamlit_style)

    # Streamlit input fields
    name = st.text_input("Name", key="name")
    email = st.text_input("Email", key="email")

    # Hidden divs to receive the messages from JavaScript
    html('<div id="hiddenEmailField"></div>')
    html('<div id="hiddenNameField"></div>')

    # Listen for messages from the JavaScript
    st.components.v1.html("""
        <script>
        window.addEventListener("message", (event) => {
            const data = event.data;
            if (data.type === 'streamlit:setEmailValue') {
                Streamlit.setComponentValue('email', data.value);
            }
            if (data.type === 'streamlit:setNameValue') {
                Streamlit.setComponentValue('name', data.value);
            }
        }, false);
        </script>
    """, height=0)

    # Button to submit the form
    submit_button = st.button("Submit")

    # Success message upon submission
    if submit_button:
        st.success(f"Form submitted with Name: {name} and Email: {email}")

if __name__ == "__main__":
    main()
    
