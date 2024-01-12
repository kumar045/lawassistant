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
    name = st.text_input("Name", value=st.session_state.name, key="name")
    email = st.text_input("Email", value=st.session_state.email, key="email")

    # Listen for postMessage events from JavaScript
    st.components.v1.html("""
        <script>
        window.addEventListener("message", (event) => {
            if (event.data.type === 'email') {
                Streamlit.setComponentValue('email', event.data.value);
            }
            if (event.data.type === 'name') {
                Streamlit.setComponentValue('name', event.data.value);
            }
        }, false);
        </script>
    """, height=0)

    # Button to submit the form
    submit_button = st.button("Submit")

    # Success message upon form submission
    if submit_button:
        st.success(f"Form submitted with Name: {name} and Email: {email}")

if __name__ == "__main__":
    main()
    
