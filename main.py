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

        .form-field {
            margin: 15px 0;
        }

        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }

        input[type="text"], input[type="submit"] {
            padding: 10px;
            margin-top: 5px;
            border-radius: 4px;
            border: 1px solid #ddd;
            width: 80%;
        }

        input[type="submit"] {
            background-color: #007bff;
            color: white;
            cursor: pointer;
            margin-top: 20px;
        }

        .submission-message {
            margin-top: 20px;
            color: green;
            font-size: 18px;
        }
    </style>
</head>
<body>
    <div class="form-container">
        <h2>Speech to Text Form</h2>
        <form id="speechForm">
            <div class="form-field">
                <label for="nameInput">Name:</label>
                <input type="text" id="nameInput" placeholder="Speak your name">
            </div>
            <div class="form-field">
                <label for="emailInput">Email:</label>
                <input type="text" id="emailInput" placeholder="Speak your email">
            </div>
            <input type="submit" value="Submit">
        </form>
        <div class="submission-message" id="submissionMessage"></div>
    </div>

    <script>
        const form = document.getElementById('speechForm');
        const nameInput = document.getElementById('nameInput');
        const emailInput = document.getElementById('emailInput');
        const submissionMessage = document.getElementById('submissionMessage');
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

        form.addEventListener('submit', (event) => {
            event.preventDefault();
            submissionMessage.textContent = 'Form submitted successfully!';
        });
    </script>
</body>
</html>



"""

def main():
    st.title("Speech Recognition Form")
    html(html_content, height=800)  # Adjust the height as necessary

if __name__ == "__main__":
    main()
    
