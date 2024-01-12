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
            document.getElementById('transcript').innerText = transcript;
            recognition.stop();

            let inputEvent = new Event('input', { bubbles: true });

            // This will need to be the ID of the Streamlit text input widget
            let nameInput = document.querySelector('input[data-baseweb="input"]');
            let emailInput = document.querySelector('input[data-baseweb="input"]');

            if (transcript.startsWith("name")) {
                let nameValue = transcript.replace("name", "").trim();
                nameInput.value = nameValue;
                nameInput.dispatchEvent(inputEvent);
            } else if (transcript.startsWith("email")) {
                let emailValue = transcript.replace("email", "").trim();
                emailInput.value = emailValue;
                emailInput.dispatchEvent(inputEvent);
            }
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

    name = st.text_input("Name", key="name")
    email = st.text_input("Email", key="email")

    submit_button = st.button("Submit")

    if submit_button:
        st.success(f"Form submitted with Name: {name} and Email: {email}")

if __name__ == "__main__":
    main()
    
