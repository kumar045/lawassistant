import streamlit as st
from streamlit.components.v1 import html

# JavaScript and HTML for Web Speech API
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
                document.getElementById('hiddenEmailField').value = email;
                document.getElementById('hiddenEmailField').dispatchEvent(new Event('input', {bubbles: true}));
            } else if (transcript.startsWith("name")) {
                var name = transcript.replace("name", "").trim();
                document.getElementById('hiddenNameField').value = name;
                document.getElementById('hiddenNameField').dispatchEvent(new Event('input', {bubbles: true}));
            }
            recognition.stop();
        };

        recognition.onerror = function(e) {
            recognition.stop();
        }
    }
}
</script>
<input type="hidden" id="hiddenEmailField" onchange="updateEmailField(this.value)" />
<input type="hidden" id="hiddenNameField" onchange="updateNameField(this.value)" />
"""

# This function will be called when the hidden field value changes
st.markdown(
    """
    <script>
    function updateEmailField(value) {
        window.parent.postMessage({type: 'streamlit:setComponentValue', value : value}, '*');
    }
    function updateNameField(value) {
        window.parent.postMessage({type: 'streamlit:setComponentValue', value : value}, '*');
    }
    </script>
    """,
    unsafe_allow_html=True,
)

def main():
    st.title("Voice Recognition Form")
    html(voice_input_script)

    # Streamlit input fields
    name = st.text_input("Name", key="name")
    email = st.text_input("Email", key="email")

    if "name" not in st.session_state:
        st.session_state.name = ""

    if "email" not in st.session_state:
        st.session_state.email = ""

    # Use the window.parent.postMessage to send the recognized value to the Streamlit server
    st.components.v1.html("""
        <script>
        window.addEventListener("message", (event) => {
            if (event.data.hasOwnProperty('type') && event.data.type === 'streamlit:setComponentValue') {
                if (event.data.hasOwnProperty('value')) {
                    if (event.data.value.includes('@')) { // Simple check to differentiate between name and email
                        Streamlit.setComponentValue({'email': event.data.value});
                    } else {
                        Streamlit.setComponentValue({'name': event.data.value});
                    }
                }
            }
        }, false);
        </script>
    """, height=0)

    submit_button = st.button("Submit")

    if submit_button:
        st.success(f"Form submitted with Name: {st.session_state.name} and Email: {st.session_state.email}")

if __name__ == "__main__":
    main()
    
