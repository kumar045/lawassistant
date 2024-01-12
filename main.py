import streamlit as st
from streamlit.components.v1 import html

# JavaScript with corrected element IDs and visual feedback
voice_input_script = """
<button onclick="startDictation()">Start Dictation</button>
<p id="transcript">Transcript will appear here...</p>
<div id="loading" style="display: none;">Loading...</div>

<script>
function startDictation() {
  document.getElementById('loading').style.display = 'block';

  if (window.hasOwnProperty('webkitSpeechRecognition')) {
    var recognition = new webkitSpeechRecognition();

    recognition.continuous = false;
    recognition.interimResults = false;
    recognition.lang = "en-US";

    setTimeout(() => recognition.start(), 500); // Brief delay for microphone activation

    recognition.onresult = function(event) {
      var transcript = event.results[0][0].transcript.trim();
      document.getElementById('transcript').innerText = transcript;
      recognition.stop();
      document.getElementById('loading').style.display = 'none';

      let inputEvent = new Event('input', { bubbles: true });

      // Correctly target Streamlit input elements using data-testid
      let nameInput = document.querySelector('input[data-testid="name"]');
      let emailInput = document.querySelector('input[data-testid="email"]');

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
      document.getElementById('loading').style.display = 'none';
      // Handle errors gracefully, e.g., display an error message
    };
  } else {
    // Handle browser compatibility issues, e.g., display a message
  }
}
</script>
"""

def main():
  st.title("Voice Recognition Form")
  html(voice_input_script)

  name = st.text_input("Name", key="name", data_testid="name")
  email = st.text_input("Email", key="email", data_testid="email")

  submit_button = st.button("Submit")

  if submit_button:
    st.success(f"Form submitted with Name: {name} and Email: {email}")

if __name__ == "__main__":
  main()
    
