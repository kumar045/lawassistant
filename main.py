import streamlit as st
from streamlit.components.v1 import html

voice_input_script = """
<button onclick="startDictation()">Start Dictation</button>
<p id="transcript">Transcript will appear here...</p>
<div id="loading" style="display: none;">Loading...</div>
<div id="email-feedback" style="display: none;"></div>
<div id="name-feedback" style="display: none;"></div>

<script>
function startDictation() {
  document.getElementById('transcript').innerText = "";
  document.getElementById('loading').style.display = 'block';
  document.getElementById('email-feedback').style.display = 'none';
  document.getElementById('name-feedback').style.display = 'none';

  if (window.hasOwnProperty('webkitSpeechRecognition')) {
    var recognition = new webkitSpeechRecognition();

    recognition.continuous = false;
    recognition.interimResults = false;
    recognition.lang = "en-US";

    setTimeout(() => recognition.start(), 500);

    recognition.onresult = function(event) {
      var transcript = event.results[0][0].transcript.trim();
      document.getElementById('transcript').innerText = transcript;
      recognition.stop();
      document.getElementById('loading').style.display = 'none';

      let inputEvent = new Event('input', { bubbles: true });

      const words = transcript.split(" ");
      let emailFound = false;
      let nameFound = false;
      let emailValue = "";
      let nameValue = "";

      for (let i = 0; i < words.length; i++) {
        if (!emailFound && words[i].toLowerCase() === "email") {
          emailFound = true;
          if (i + 1 < words.length) {
            emailValue = words.slice(i + 1).join(" ");
            break;
          }
        } else if (!nameFound && words[i].toLowerCase() === "name") {
          nameFound = true;
          if (i + 1 < words.length) {
            nameValue = words.slice(i + 1).join(" ");
            break;
          }
        }
      }

      if (emailValue) {
        let emailInput = document.querySelector(`input[id="${st.session_state.email}"]`);
        emailInput.value = emailValue;
        emailInput.dispatchEvent(inputEvent);
        document.getElementById('email-feedback').style.display = 'block';
        document.getElementById('email-feedback').innerText = "Email field updated.";
      }
      if (nameValue) {
        let nameInput = document.querySelector(`input[id="${st.session_state.name}"]`);
        nameInput.value = nameValue;
        nameInput.dispatchEvent(inputEvent);
        document.getElementById('name-feedback').style.display = 'block';
        document.getElementById('name-feedback').innerText = "Name field updated.";
      }
    };

    recognition.onerror = function(event) {
      recognition.stop();
      document.getElementById('loading').style.display = 'none';
    };
  } else {
    // Handle browser compatibility issues
  }
}
</script>
"""

def main():
  st.title("Voice-Enabled Form with Refined Features")
  html(voice_input_script)

  name_input = st.text_input("Name", key="name")
  email_input = st.text_input("Email", key="email")

if __name__ == "__main__":
  main()
  
