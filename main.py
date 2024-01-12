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
            var words = transcript.split(' ');
            var command = words.shift().toLowerCase();
            var restOfSpeech = words.join(' ');

            document.getElementById('transcript').innerText = transcript;

            if (command === "email") {
                window.parent.postMessage({type: 'email', value: restOfSpeech}, '*');
            } else if (command === "name") {
                window.parent.postMessage({type: 'name', value: restOfSpeech}, '*');
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

    # Create session_state keys for name and email
    if 'email' not in st.session_state:
        st.session_state.email = ""
    if 'name' not in st.session_state:
        st.session_state.name = ""

    # Display input fields
    name = st.text_input("Name", value=st.session_state.name)
    email = st.text_input("Email", value=st.session_state.email)

    # Listen for postMessage events from JavaScript
    st.components.v1.html("""
        <script>
        window.addEventListener("message", (event) => {
            if (event.data.type === 'email') {
                Streamlit.setComponentValue('email_input', event.data.value);
            }
            if (event.data.type === 'name') {
                Streamlit.setComponentValue('name_input', event.data.value);
            }
        }, false);
        </script>
    """, height=0)

    # Button to submit the form
    submit_button = st.button("Submit")

    # Success message upon form submission
    if submit_button:
        st.success(f"Form submitted with Name: {st.session_state.name} and Email: {st.session_state.email}")

    # Callbacks to update session_state when new values are set
    def on_email_change():
        st.session_state.email = st.session_state.email_input

    def on_name_change():
        st.session_state.name = st.session_state.name_input

    # Hidden fields to trigger callbacks
    st.text_input("", value="", key="email_input", on_change=on_email_change, args=(), type="default", hidden=True)
    st.text_input("", value="", key="name_input", on_change=on_name_change, args=(), type="default", hidden=True)

if __name__ == "__main__":
    main()
    
