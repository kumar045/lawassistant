import streamlit as st
from streamlit_webrtc import webrtc_streamer, WebRtcMode, RTCConfiguration
import speech_recognition as sr

# This is needed if you're running the app in a network environment
RTC_CONFIGURATION = RTCConfiguration({"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]})

def main():
    st.header("Real-time speech recognition with Streamlit")

    webrtc_ctx = webrtc_streamer(
        key="speech-to-text",
        mode=WebRtcMode.SENDONLY,
        rtc_configuration=RTC_CONFIGURATION,
        audio_receiver_size=256,
        async_processing=True,
    )

    if webrtc_ctx.state.playing:
        st.markdown("Speak something...")
        labels_placeholder = st.empty()
        while True:
            if webrtc_ctx.audio_receiver:
                try:
                    audio_chunk = webrtc_ctx.audio_receiver.get_frame(timeout=1)
                except queue.Empty:
                    continue
                audio_data = pydub.AudioSegment(
                    data=audio_chunk.to_bytes(), sample_width=audio_chunk.format.bytes, frame_rate=audio_chunk.sample_rate, channels=len(audio_chunk.layout.channels)
                )
                r = sr.Recognizer()
                with sr.AudioData(audio_data.raw_data, audio_data.frame_rate, audio_data.sample_width) as source:
                    text = r.recognize_google(source, language="en-US")
                    labels_placeholder.markdown(f"Recognized Text: {text}")
    else:
        st.markdown("Please start the audio stream")

if __name__ == "__main__":
    main()
    
