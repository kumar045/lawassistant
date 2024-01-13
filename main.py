import streamlit as st
from streamlit.components.v1 import html

# Combining your HTML, CSS, and JavaScript into a single HTML content
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100vh;
            margin: 0;
        }

        .container {
            text-align: center;
            background-color: white;
            border-radius: 8px;
            padding: 20px;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
        }

        .title {
            color: #333;
            margin-bottom: 20px;
        }

        .recordButton {
            background-color: #007bff;
            color: white;
            border: none;
            border-radius: 4px;
            padding: 10px 20px;
            cursor: pointer;
            font-size: 16px;
            transition: background-color 0.3s ease;
        }

        .recordButton:hover {
            background-color: #0056b3;
        }

        .outputText {
            margin-top: 20px;
            padding: 10px;
            background-color: #f5f5f5;
            border: 1px solid #ddd;
            border-radius: 4px;
            min-height: 100px;
            font-size: 18px;
        }
    </style>
    <title>Speech to Text</title>
</head>
<body>
    <div class="container">
        <h1 class="title">Speech to Text</h1>
        <button id="startButton" class="recordButton">Start Recording</button>
        <div id="output" class="outputText"></div>
    </div>

    <script>
        const startButton = document.getElementById('startButton');
        const outputDiv = document.getElementById('output');
        const recognition = new webkitSpeechRecognition() || new SpeechRecognition();

        recognition.interimResults = true;
        recognition.continuous = true;

        startButton.addEventListener('click', () => {
            recognition.start();
            startButton.disabled = true;
            startButton.textContent = 'Recording...';
        });

        recognition.onresult = event => {
            const result = event.results[event.results.length - 1][0].transcript;
            outputDiv.textContent = result;
        };

        recognition.onend = () => {
            startButton.disabled = false;
            startButton.textContent = 'Start Recording';
        };

        recognition.onerror = event => {
            console.error('Speech recognition error:', event.error);
        };

        recognition.onnomatch = () => {
            console.log('No speech was recognized.');
        };
    </script>
</body>
</html>


"""

def main():
    st.title("Speech Recognition Form")
    html(html_content, height=800)  # Adjust the height as necessary

if __name__ == "__main__":
    main()
    
