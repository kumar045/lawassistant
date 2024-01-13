import streamlit as st
from streamlit.components.v1 import html

# Combining your HTML, CSS, and JavaScript into a single HTML content
html_content = """
<!DOCTYPE html>

<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Speech to Text Form</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100vh;
            margin: 0;
        }

        .form-container {
            text-align: center;
            border: 1px solid #ddd;
            padding: 20px;
            border-radius: 8px;
        }

        input[type="text"] {
            padding: 10px;
            margin: 10px 0;
            border-radius: 4px;
            border: 1px solid #ddd;
            width: 80%;
        }
    </style>
</head>
<body>
    <div class="form-container">
        <h2>Speech to Text Form</h2>
        <input type="text" id="nameInput" placeholder="Speak your name">
        <input type="text" id="emailInput" placeholder="Speak your email">
    </div>

    <script>
        const nameInput = document.getElementById('nameInput');
        const emailInput = document.getElementById('emailInput');
        const recognition = new webkitSpeechRecognition() || new SpeechRecognition();
        let currentInput;

        recognition.interimResults = false;
        recognition.continuous = false;

        nameInput.addEventListener('click', () => {
            currentInput = nameInput;
            recognition.start();
        });

        emailInput.addEventListener('click', () => {
            currentInput = emailInput;
            recognition.start();
        });

        recognition.onresult = event => {
            const result = event.results[0][0].transcript;
            currentInput.value = result;
        };

        recognition.onend = () => {
            recognition.stop();
        };

        recognition.onerror = event => {
            console.error('Speech recognition error:', event.error);
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
    
