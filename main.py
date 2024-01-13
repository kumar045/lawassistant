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
        * { box-sizing: border-box; }
        body { --gap: 1rem; font-family: ui-sans-serif, system-ui, sans-serif; }
        button { background-color: hsl(90, 50%, 30%); border: 0; color: hsl(90, 50%, 95%); margin-block-start: var(--gap); padding: calc(var(--gap) / 2) var(--gap); }
        button.listening { background-color: hsl(0, 50%, 50%); color: hsl(0, 50%, 95%); }
        code { background: #333; color: lime; display: block; padding: calc(var(--gap) / 2); }
        fieldset { background: #EEE; border: 1px solid #BBB; padding: var(--gap); }
        form { margin: 0 auto; max-width: 30rem; }
        input, textarea { border: 1px solid #BBB; display: block; padding: calc(var(--gap) / 2); resize: vertical; width: 100%; }
        label { display: block; font-weight: 500; margin-block-start: var(--gap); }
        p { font-size: small; }
    </style>
</head>
<body>
    <form>
        <fieldset>
            <legend>Fill Out Form With Speech Recognition (Chrome)</legend>
            <code id="result">live transcript here ...</code>
            <button type="button" id="toggle">Toggle listening</button>
            <p>Click on “Toggle listening”, then click on the form field, where you want to insert speeched text. Pause a bit after a sentence to process the speech-data. This demo only works with language <strong>“en-US”</strong>, only in Chrome, and only if you allow the microphone on this page!</p>
            <label>Field 1<input /></label>
            <label>Field 2<input /></label>
            <label>Field 3<input /></label>
            <label>Field 4<textarea></textarea></label>
        </fieldset>
    </form>
    <script>
        function init() {
            window.SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
            if (('SpeechRecognition' in window || 'webkitSpeechRecognition' in window)) {
                let speech = { enabled: true, listening: false, recognition: new window.SpeechRecognition(), text: '' }
                speech.recognition.continuous = true;
                speech.recognition.interimResults = true;
                speech.recognition.lang = 'en-US';
                speech.recognition.addEventListener('result', (event) => {
                    const audio = event.results[event.results.length - 1];
                    speech.text = audio[0].transcript;
                    const tag = document.activeElement.nodeName;
                    if (tag === 'INPUT' || tag === 'TEXTAREA') {
                        if (audio.isFinal) {
                            document.activeElement.value += speech.text;
                        }
                    }
                    result.innerText = speech.text;
                });

                toggle.addEventListener('click', () => {
                    speech.listening = !speech.listening;
                    if (speech.listening) {
                        toggle.classList.add('listening');
                        toggle.innerText = 'Listening ...';
                        speech.recognition.start();
                    } else {
                        toggle.classList.remove('listening');
                        toggle.innerText = 'Toggle listening';
                        speech.recognition.stop();
                    }
                });
            }
        }
        window.onload = init;
    </script>
</body>
</html>
"""

def main():
    st.title("Speech Recognition Form")
    html(html_content, height=800)  # Adjust the height as necessary

if __name__ == "__main__":
    main()
    
