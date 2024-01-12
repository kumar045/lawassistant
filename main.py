import streamlit as st
from streamlit.components.v1 import html

# JavaScript and HTML for Web Speech API
voice_input_script = """
<div>
    <button onclick="startDictation()">Start Dictation</button>
    <p id="transcript">Transcript will appear here...</p>
</div>

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
                document.getElementById('voiceInputEmail').value = transcript.replace("email", "").trim();
                let eventEmail = new Event('input', { bubbles: true });
                document.getElementById('voiceInputEmail').dispatchEvent(eventEmail);
            } else if (transcript.startsWith("name")) {
                document.getElementById('voiceInputName').value = transcript.replace("name", "").trim();
                let eventName = new Event('input', { bubbles: true });
                document.getElementById('voiceInputName').dispatchEvent(eventName);
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

def main():
    st.title("Voice Recognition Form")

    # Custom HTML for voice input
    html(voice_input_script)

    # Hidden text areas to capture voice input for each field
    voice_input_email = st.text_area("Voice Email", "", key="voiceInputEmail", height=0)
    voice_input_name = st.text_area("Voice Name", "", key="voiceInputName", height=0)

    # Streamlit form fields
    name = st.text_input("Name", key="name", value=voice_input_name)
    email = st.text_input("Email", key="email", value=voice_input_email)

    submit_button = st.button("Submit")

    if submit_button:
        st.success(f"Form submitted with Name: {name} and Email: {email}")

if __name__ == "__main__":
    main()
    
