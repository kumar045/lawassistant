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

def main():
    st.title("Voice Recognition Form")
    html(voice_input_script)

    # Use Streamlit session state to hold the values for name and email
    if 'email' not in st.session_state:
        st.session_state.email = ""
    if 'name' not in st.session_state:
        st.session_state.name = ""

    # Streamlit input fields
    name = st.text_input("Name", value=st.session_state.name)
    email = st.text_input("Email", value=st.session_state.email)

    # Button to submit the form
    submit_button = st.button("Submit")

    # Success message upon submission
    if submit_button:
        st.success(f"Form submitted with Name: {name} and Email: {email}")

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

    # Callbacks to update Streamlit session state when values are received from JavaScript
    def on_email_change():
        st.session_state.email = st.session_state.email_input

    def on_name_change():
        st.session_state.name = st.session_state.name_input

    # Create callbacks
    st.text_input("hidden_email_input", key="email_input", on_change=on_email_change, args=(), type="hidden")
    st.text_input("hidden_name_input", key="name_input", on_change=on_name_change, args=(), type="hidden")

if __name__ == "__main__":
    main()
