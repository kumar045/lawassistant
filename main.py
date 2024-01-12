import streamlit as st
from streamlit_webrtc import webrtc_streamer, WebRtcMode, RTCConfiguration
import speech_recognition as sr
import queue  # Import the queue module

# This is needed if you're running the app in a network environment
RTC_CONFIGURATION = RTCConfiguration({"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]})

def main():
    st.header("Real-time speech recognition with Streamlit")

    # Set a larger buffer size if needed
    webrtc_ctx = webrtc_streamer(
        key="speech-to-text",
        mode=WebRtcMode.SENDONLY,
        rtc_configuration=RTC_CONFIGURATION,
        audio_receiver_size=1024,  # Increase the receiver size if necessary
        async_processing=True,
    )

    if webrtc_ctx.state.playing:
        st.markdown("Speak something...")
        labels_placeholder = st.empty()

        audio_processor = AudioProcessor(webrtc_ctx.audio_receiver)
        audio_processor.start()

        while True:
            if audio_processor.has_new_text():
                text = audio_processor.get_text()
                labels_placeholder.markdown(f"Recognized Text: {text}")

class AudioProcessor:
    def __init__(self, audio_receiver):
        self.audio_receiver = audio_receiver
        self.recognizer = sr.Recognizer()
        self.text = ""
        self.new_text_available = False

    def start(self):
        while True:
            try:
                audio_chunk = self.audio_receiver.get_frame(timeout=1)
                self.process_audio_chunk(audio_chunk)
            except queue.Empty:
                continue

    def process_audio_chunk(self, audio_chunk):
        audio_data = sr.AudioData(
            audio_chunk.to_bytes(),
            audio_chunk.sample_rate,
            audio_chunk.sample_width
        )
        try:
            text = self.recognizer.recognize_google(audio_data, language="en-US")
            self.text = text
            self.new_text_available = True
        except sr.UnknownValueError:
            pass  # Handle the exception if the speech is unintelligible
        except sr.RequestError as e:
            pass  # Handle the exception if the API is unreachable

    def has_new_text(self):
        return self.new_text_available

    def get_text(self):
        self.new_text_available = False
        return self.text

if __name__ == "__main__":
    main()
    
