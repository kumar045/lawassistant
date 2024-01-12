import streamlit as st
from streamlit.components.v1 import html

# HTML and JavaScript for integrating Annyang for voice commands
voice_input_html = """
<html>
<head>
<script src="https://cdnjs.cloudflare.com/ajax/libs/annyang/2.6.1/annyang.min.js"></script>
</head>
<body>
<script>
function startCommand() {
    if (annyang) {
        annyang.start({ continuous: false });

        annyang.addCallback('result', function(phrases) {
            document.getElementById('voiceInput').value = phrases[0];
            annyang.abort();
        });
    }
}
</script>
<input type="text" id="voiceInput" placeholder="Speak to fill this field" readonly>
<button onclick="startCommand()">Start Voice Input</button>
</body>
</html>
"""

def main():
    st.title("Voice Input Form")

    # Display the custom HTML for voice input
    html(voice_input_html, height=150)

    # Use Streamlit to create other form elements
    name = st.text_input("Name", key="name")
    email = st.text_input("Email", key="email")
    submit_button = st.button("Submit")

    if submit_button:
        st.success(f"Form submitted with Name: {name} and Email: {email}")

if __name__ == "__main__":
    main()
