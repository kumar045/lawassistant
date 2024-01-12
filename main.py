import streamlit as st
import speech_recognition as sr

# Initialize the speech recognizer
r = sr.Recognizer()

def recognize_speech_from_audio(uploaded_audio):
    with sr.AudioFile(uploaded_audio) as source:
        audio_data = r.record(source)
        # recognize speech using Google Web Speech API
        try:
            text = r.recognize_google(audio_data)
            return text
        except sr.UnknownValueError:
            return "Google Web Speech API could not understand the audio"
        except sr.RequestError:
            return "Could not request results from Google Web Speech API"

def main():
    st.title("Speech Recognition with Streamlit")
    
    uploaded_file = st.file_uploader("Upload Audio File", type=['wav', 'flac', 'mp3', 'ogg'])

    if uploaded_file is not None:
        if st.button('Transcribe'):
            # Process the uploaded audio file
            text = recognize_speech_from_audio(uploaded_file)
            st.text_area("Transcribed Text:", value=text, height=150)

if __name__ == "__main__":
    main()
    
