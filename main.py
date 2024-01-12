import streamlit as st
from streamlit.components.v1 import html

# JavaScript and HTML for Annyang
voice_input_script = """
<script src="https://cdnjs.cloudflare.com/ajax/libs/annyang/2.6.1/annyang.min.js"></script>
<script>
function startVoiceRecognition() {
    if (annyang) {
        var commands = {
            'name *tag': function(tag) {
                document.getElementById("voiceInput").value = "name," + tag;
                let event = new Event('input', { bubbles: true });
                document.getElementById("voiceInput").dispatchEvent(event);
            },
            'email *tag': function(tag) {
                document.getElementById("voiceInput").value = "email," + tag.replace(/\s/g, '');
                let event = new Event('input', { bubbles: true });
                document.getElementById("voiceInput").dispatchEvent(event);
            }
        };

        annyang.addCommands(commands);
        annyang.start();
    }
}
</script>
<button onclick="startVoiceRecognition()">Start Voice Recognition</button>
<textarea id="voiceInput" style="display:none;"></textarea>
"""

def main():
    st.title("Voice Input Form")
    html(voice_input_script)

    # Hidden text area to capture voice input
    voice_input = st.text_area("Voice Input", "", key="voice_input", height=0)

    # Parse the voice input and assign to Streamlit fields
    if voice_input:
        input_type, input_value = voice_input.split(",", 1)
        if input_type == "name":
            st.session_state.name = input_value
        elif input_type == "email":
            st.session_state.email = input_value

    # Streamlit form fields
    name = st.text_input("Name", key="name", value=st.session_state.get("name", ""))
    email = st.text_input("Email", key="email", value=st.session_state.get("email", ""))
    submit_button = st.button("Submit")

    if submit_button:
        st.success(f"Form submitted with Name: {name} and Email: {email}")

if __name__ == "__main__":
    main()
    
