# Voice-to-Text, LLM Summarization, and Text-to-Speech(End to End Audio Summaraizer)

This Streamlit application combines voice-to-text transcription, LLM-based summarization, and text-to-speech synthesis to process audio files and generate concise summaries.

## Features

- Upload audio files (WAV, MP3, OGG)
- Voice Activity Detection (VAD) for improved transcription
- Transcribe audio to text using Whisper model
- Summarize transcriptions using BART-large-CNN model
- Convert summaries to speech with adjustable pitch, speed, and voice gender
- Interactive Streamlit interface

## Requirements

- Python 3.7+
- Streamlit
- NumPy
- SoundFile
- faster-whisper
- SciPy
- transformers
- pyttsx3

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/vrtteja002/AI_Lizmotors_Intern_Task
   cd voice-text-summary-speech
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

2. Open your web browser and go to the URL displayed in the terminal (usually `http://localhost:8501`).

3. Use the interface to:
   - Upload an audio file
   - Adjust the VAD threshold
   - Modify pitch, speed, and voice gender for text-to-speech
   - Click "Transcribe, Summarize, and Speak" to process the audio

4. View the transcription, summary, and listen to the synthesized speech of the summary.

## Configuration

- VAD Threshold: Adjust the sensitivity of the Voice Activity Detection (0.0 to 1.0)
- Pitch: Modify the pitch of the synthesized voice (-50 to 50)
- Speed: Change the speed of the synthesized voice (50 to 300 words per minute)
- Voice Gender: Choose between male and female voices

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
