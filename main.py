import streamlit as st
from streamlit.components.v1 import html

# JavaScript with improved transcript parsing, visual feedback, and error handling
voice_input_script = """
<button onclick="startDictation()">Start Dictation</button>
<p id="transcript">Transcript will appear here...</p>
<div id="loading" style="display: none;">Loading...</div>
<div id="email-feedback" style="display: none;"></div>  <script>
function startDictation() {
  document.getElementById('transcript').innerText = "";  // Clear transcript before starting
  document.getElementById('loading').style.display = 'block';
  document.getElementById('email-feedback').style.display = 'none';

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

      // Stricter pattern matching for "email"
      const emailMatch = transcript.match(/^email\s+(.+)/i);
      if (emailMatch) {
        let emailValue = emailMatch[1].trim();
        let emailInput = document.querySelector(`input[id="${st.session_state.email}"]`);
        emailInput.value = emailValue;
        emailInput.dispatchEvent(inputEvent);
        document.getElementById('email-feedback').style.display = 'block';  // Show feedback
        document.getElementById('email-feedback').innerText = "Email field updated with spoken address.";
      } else {
        // Handle other cases or errors
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

  name = st.text_input("Name", key="name")
  email = st.text_input("Email", key="email")

  submit_button = st.button("Submit")

  if submit_button:
    st.success(f"Form submitted with Name: {name} and Email: {email}")

if __name__ == "__main__":
  main()
  
