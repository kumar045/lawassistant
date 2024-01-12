import streamlit as st
from streamlit.components.v1 import html

# JavaScript for Web Speech API integration
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

        recognition.onresult = function(event) {
            var transcript = event.results[0][0].transcript.trim();
            var command = transcript.split(' ')[0].toLowerCase();
            var value = transcript.substring(command.length).trim();

            document.getElementById('transcript').innerText = transcript;

            if (command === "email") {
                window.parent.postMessage({type: 'streamlit:update', field: 'email', value: value}, '*');
            } else if (command === "name") {
                window.parent.postMessage({type: 'streamlit:update', field: 'name', value: value}, '*');
            }

            recognition.stop();
        };

        recognition.onerror = function(event) {
            recognition.stop();
        }
    }
}
</script>
"""

def main():
    st.title("Voice Recognition Form")
    html(voice_input_script)

    # Input fields for name and email
    name = st.text_input("Name", key="name")
    email = st.text_input("Email", key="email")

    # Button to submit the form
    submit_button = st.button("Submit")

    # Success message upon form submission
    if submit_button:
        st.success(f"Form submitted with Name: {name} and Email: {email}")

    # Listen for messages from the JavaScript and update the input fields
    st.components.v1.html("""
        <script>
        window.addEventListener("message", (event) => {
            if (event.data.type === 'streamlit:update') {
                if (event.data.field === 'email') {
                    Streamlit.setComponentValue('email', event.data.value);
                } else if (event.data.field === 'name') {
                    Streamlit.setComponentValue('name', event.data.value);
                }
            }
        }, false);
        </script>
    """, height=0)

if __name__ == "__main__":
    main()
    
