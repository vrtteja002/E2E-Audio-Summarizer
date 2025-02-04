import streamlit as st
import numpy as np
import soundfile as sf
from faster_whisper import WhisperModel
from scipy import signal
import tempfile
import os
from transformers import pipeline
import io
import pyttsx3
os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'
os.environ['OMP_NUM_THREADS'] = '1'

def voice_activity_detection(audio, sample_rate, threshold=0.0, frame_length=1024, hop_length=512):
    energy = np.array([
        sum(abs(audio[i:i+frame_length]**2))
        for i in range(0, len(audio), hop_length)
    ])
    energy_normalized = (energy - np.min(energy)) / (np.max(energy) - np.min(energy))
    voice_activity = energy_normalized > threshold
    voice_activity_expanded = np.repeat(voice_activity, hop_length)[:len(audio)]
    return voice_activity_expanded

def preprocess_audio(audio, sr, target_sr=16000):
    if audio.ndim > 1:
        audio = audio.mean(axis=1)
    if sr != target_sr:
        audio = signal.resample(audio, int(len(audio) * target_sr / sr))
    return audio, target_sr

def voice_to_text(audio, sr, vad_threshold=0.5):
    audio, sample_rate = preprocess_audio(audio, sr)
    voice_activity = voice_activity_detection(audio, sample_rate, threshold=vad_threshold)
    audio_vad = audio * voice_activity
    model = WhisperModel("base", device="cpu", compute_type="int8")
    segments, _ = model.transcribe(audio_vad, beam_size=5)
    transcription = " ".join([segment.text for segment in segments])
    return transcription

@st.cache_resource
def load_summarizer():
    return pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_with_llm(text):
    summarizer = load_summarizer()
    summary = summarizer(text, max_length=60, min_length=30, do_sample=True)[0]['summary_text']
    sentences = summary.split('.')
    return '. '.join(sentences[:3]).strip() + '.'

def text_to_speech(text, pitch=0, speed=150, voice_gender='male'):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    
    voice = voices[1] if voice_gender == 'female' else voices[0]
    engine.setProperty('voice', voice.id)
    
    engine.setProperty('rate', speed)
    
    # Adjust pitch using SetProperty method
    engine.setProperty('pitch', pitch)
    
    fp = io.BytesIO()
    engine.save_to_file(text, 'temp.wav')
    engine.runAndWait()
    
    with open('temp.wav', 'rb') as f:
        fp.write(f.read())
    
    os.remove('temp.wav')
    fp.seek(0)
    return fp

def main():
    st.title("Voice-to-Text, LLM Summarization, and Text-to-Speech")

    uploaded_file = st.file_uploader("Choose an audio file", type=["wav", "mp3", "ogg"])

    vad_threshold = st.slider("VAD Threshold", 0.0, 1.0, 0.5, 0.01)
    pitch = st.slider("Pitch", -50, 50, 0)
    speed = st.slider("Speed", 50, 300, 150)
    voice_gender = st.selectbox("Voice Gender", ["male", "female"])

    if uploaded_file is not None:
        st.audio(uploaded_file, format="audio/wav")

        if st.button("Transcribe, Summarize, and Speak"):
            with st.spinner("Processing..."):
                try:
                    with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[1]) as tmp_file:
                        tmp_file.write(uploaded_file.getvalue())
                        tmp_file_path = tmp_file.name

                    audio, sr = sf.read(tmp_file_path)
                    os.unlink(tmp_file_path)

                    transcription = voice_to_text(audio, sr, vad_threshold)

                    st.subheader("Transcription:")
                    st.write(transcription)

                    summary = summarize_with_llm(transcription)

                    st.subheader("Summary (2-3 sentences):")
                    st.write(summary)

                    summary_audio = text_to_speech(summary, pitch=pitch, speed=speed, voice_gender=voice_gender)

                    st.subheader("Summary Audio:")
                    st.audio(summary_audio, format="audio/wav")

                except FileNotFoundError:
                    st.error("Error: The uploaded file could not be found. Please try uploading again.")
                except sf.SoundFileError:
                    st.error("Error: The uploaded file is not a valid audio file. Please upload a WAV, MP3, or OGG file.")
                except Exception as e:
                    st.error(f"An unexpected error occurred: {str(e)}")

    st.markdown("---")
if __name__ == "__main__":
    main()
