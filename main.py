import streamlit as st
from streamlit.components.v1 import html

# Define the entire HTML content
html_content = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        #container {
            padding: 20px;
        }
        button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            margin: 10px 0;
            border: none;
            cursor: pointer;
        }
        button:hover {
            background-color: #45a049;
        }
        p, .feedback {
            margin: 10px 0;
        }
    </style>
</head>
<body>
    <div id="container">
        <button onclick="startDictation()">Start Dictation</button>
        <p id="transcript">Transcript will appear here...</p>
        <div id="loading" style="display: none;">Loading...</div>
        <div id="email-feedback" class="feedback" style="display: none;"></div>
        <div id="name-feedback" class="feedback" style="display: none;"></div>
    </div>

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

                    // Process transcript (example logic here)
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
</body>
</html>
"""

def main():
    st.title("Custom Form in Streamlit")
    html(html_content)

if __name__ == "__main__":
    main()
  
