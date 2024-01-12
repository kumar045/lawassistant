import streamlit as st
from streamlit.components.v1 import html

# JavaScript and HTML for Annyang
voice_input_script = """
<script src="https://cdnjs.cloudflare.com/ajax/libs/annyang/2.6.1/annyang.min.js"></script>
<script>
function startVoiceRecognition() {
    if (annyang) {
        // Define commands
        var commands = {
            'name *tag': function(tag) {
                document.getElementById("name").value = tag;
                let name_event = new Event('input', { bubbles: true });
                document.getElementById("name").dispatchEvent(name_event);
            },
            'email *tag': function(tag) {
                document.getElementById("email").value = tag.replace(/\s/g, '');
                let email_event = new Event('input', { bubbles: true });
                document.getElementById("email").dispatchEvent(email_event);
            }
        };

        annyang.addCommands(commands);
        annyang.start();
    }
}
</script>
<button onclick="startVoiceRecognition()">Start Voice Recognition</button>
"""

def main():
    st.title("Voice Input Form")

    # Display the button for voice recognition
    html(voice_input_script)

    # Streamlit form fields
    name = st.text_input("Name", key="name", id="name")
    email = st.text_input("Email", key="email", id="email")
    submit_button = st.button("Submit")

    if submit_button:
        st.success(f"Form submitted with Name: {name} and Email: {email}")

if __name__ == "__main__":
    main()
