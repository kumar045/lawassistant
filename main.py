import streamlit as st
from streamlit.components.v1 import html

# Complete HTML with embedded CSS and JavaScript for the Web Speech API
voice_input_script = """
<style>
button {
    margin: 10px 0;
    padding: 10px 20px;
    font-size: 16px;
}

#transcript {
    margin-top: 10px;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
}
</style>

<button id="start_button" onclick="startDictation()">Start Dictation</button>
<p id="transcript">Transcript will appear here...</p>

<script>
function startDictation() {
    if (window.hasOwnProperty('webkitSpeechRecognition')) {
        var recognition = new webkitSpeechRecognition();

        recognition.continuous = false; // Set to false to stop recognition after a short phrase
        recognition.interimResults = false; // We don't want interim results
        recognition.lang = "en-US";
        recognition.start();

        // Handle the end of a speech recognition session
        recognition.onresult = function(event) {
            var transcript = event.results[0][0].transcript.trim();
            var command = transcript.split(' ')[0].toLowerCase();
            var value = transcript.substring(command.length).trim();

            document.getElementById('transcript').innerText = transcript;
            recognition.stop();

            // Post the message to the Streamlit app
            if (command === "email") {
                window.parent.postMessage({type: 'streamlit:update', field: 'email', value: value}, '*');
            } else if (command === "name") {
                window.parent.postMessage({type: 'streamlit:update', field: 'name', value: value}, '*');
            }
        };

        recognition.onerror = function(event) {
            recognition.stop();
        }
    } else {
        document.getElementById('transcript').innerText = "Web Speech API is not supported in this browser.";
    }
}
</script>
"""

def main():
    st.title("Voice Recognition Form")
    html(voice_input_script, height=300)

    # Use the session state to store the values of name and email
    if 'email' not in st.session_state:
        st.session_state['email'] = ""
    if 'name' not in st.session_state:
        st.session_state['name'] = ""

    # Display input fields
    name = st.text_input("Name", value=st.session_state['name'], key="name")
    email = st.text_input("Email", value=st.session_state['email'], key="email")

    # Button to submit the form
    submit_button = st.button("Submit")

    # Success message upon form submission
    if submit_button:
        st.success(f"Form submitted with Name: {name} and Email: {email}")

    # JavaScript message event listener
    event_listener_script = """
        <script>
        window.addEventListener("message", (event) => {
            if (event.data.type === 'streamlit:update') {
                if (event.data.field === 'email') {
                    Streamlit.setSessionState({'email': event.data.value});
                } else if (event.data.field === 'name') {
                    Streamlit.setSessionState({'name': event.data.value});
                }
            }
        }, false);
        </script>
    """

    # Insert the event listener in the app
    html(event_listener_script, height=0)

    # Check for updates from JavaScript messages and rerun the app to update the inputs
    if 'update' in st.session_state:
        name = st.session_state['name']
        email = st.session_state['email']
        del st.session_state['update']  # Clear the update flag
        st.experimental_rerun()

if __name__ == "__main__":
    main()
    
