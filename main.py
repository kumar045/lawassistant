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
            document.getElementById('transcript').innerText = e.results[0][0].transcript;
            recognition.stop();
            document.getElementById('voiceInput').value = e.results[0][0].transcript;
            let event = new Event('input', { bubbles: true });
            document.getElementById('voiceInput').dispatchEvent(event);
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

    # Hidden text area to capture voice input
    voice_input = st.text_area("Voice Input", "", key="voice_input", height=0)

    # Display the captured text
    if voice_input:
        st.write("You said: ", voice_input)

    # More Streamlit app code can go here...

if __name__ == "__main__":
    main()
    
