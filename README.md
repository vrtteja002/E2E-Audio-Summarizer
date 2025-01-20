# End-to-End Audio Summarizer

## Overview

This Streamlit application provides an end-to-end solution for audio summarization, combining voice-to-text transcription, LLM-based summarization, and text-to-speech synthesis. It processes audio files to generate concise, spoken summaries, making it ideal for quickly extracting key information from audio content.

## Table of Contents

- [Features](#features)
- [Architecture](#architecture)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [How It Works](#how-it-works)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Audio Upload**: Support for WAV, MP3, and OGG file formats
- **Voice Activity Detection (VAD)**: Enhances transcription accuracy by focusing on speech segments
- **Speech-to-Text**: Utilizes the Whisper model for accurate transcription
- **Text Summarization**: Employs the BART-large-CNN model for concise summarization
- **Text-to-Speech**: Converts summaries back to audio with customizable voice settings
- **Interactive UI**: User-friendly Streamlit interface for easy operation

## Architecture

The architecture of the End-to-End Audio Summarizer is illustrated in the diagram below:

```mermaid
graph TD
    A[User Interface] -->|Upload Audio| B[Audio Input]
    B --> C[Voice Activity Detection]
    C --> D[Speech-to-Text Transcription]
    D --> E[LLM-based Summarization]
    E --> F[Text-to-Speech Synthesis]
    F --> G[Audio Output]

    H[Configuration] -->|VAD Threshold| C
    H -->|Pitch, Speed, Voice Gender| F

    subgraph Streamlit App
    A
    H
    end

    subgraph Processing Pipeline
    B
    C
    D
    E
    F
    G
    end

    subgraph Models
    I[Whisper Model]
    J[BART-large-CNN]
    K[pyttsx3 Engine]
    end

    D -.->|Uses| I
    E -.->|Uses| J
    F -.->|Uses| K
```

This diagram illustrates the flow of data through the application:
1. The user uploads an audio file through the Streamlit interface.
2. The audio undergoes Voice Activity Detection to isolate speech segments.
3. The Whisper model transcribes the speech to text.
4. The BART-large-CNN model summarizes the transcription.
5. The pyttsx3 engine converts the summary back to speech.
6. The final audio summary is presented to the user.

The diagram also shows how user configurations (VAD threshold, TTS settings) influence different stages of the process.

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

1. Clone the repository:
   ```bash
   git clone https://github.com/vrtteja002/E2E-Audio-Summarizer.git 
   cd E2E-Audio-Summarizer
   ```

2. Set up a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Launch the Streamlit app:
   ```bash
   streamlit run app.py
   ```

2. Access the application in your web browser (typically at `http://localhost:8501`).

3. Use the interface to:
   - Upload an audio file (WAV, MP3, or OGG format)
   - Adjust the VAD threshold using the slider
   - Customize TTS settings (pitch, speed, voice gender)
   - Click "Transcribe, Summarize, and Speak" to process the audio

4. Review the results:
   - Read the full transcription
   - View the generated summary (2-3 sentences)
   - Listen to the synthesized summary audio

## Configuration

- **VAD Threshold**: Fine-tune Voice Activity Detection sensitivity (range: 0.0 to 1.0)
- **TTS Pitch**: Adjust voice pitch (-50 to 50)
- **TTS Speed**: Modify speech rate (50 to 300 words per minute)
- **Voice Gender**: Select male or female voice for TTS output

## How It Works

1. **Voice Activity Detection**: Identifies speech segments in the audio using energy-based thresholding
2. **Transcription**: Converts speech to text using the Whisper model (base version)
3. **Summarization**: Condenses the transcription using BART-large-CNN model
4. **Text-to-Speech**: Generates an audio version of the summary using pyttsx3

## Troubleshooting

- If you encounter OMP or KMP errors, set these environment variables:
  ```bash
  export KMP_DUPLICATE_LIB_OK=TRUE
  export OMP_NUM_THREADS=1
  ```
- Ensure all dependencies are correctly installed and your Python version is compatible
- For audio playback issues, check your system's audio settings and browser compatibility
- If the summarization seems off, try adjusting the VAD threshold or check the audio quality

## Contributing

We welcome contributions to improve the End-to-End Audio Summarizer! Please follow these steps:

1. Fork the repository
2. Create a new branch for your feature or bug fix
3. Commit your changes with clear, descriptive messages
4. Push the branch and open a pull request with a detailed description of your changes

Before submitting a pull request, please ensure your code adheres to the project's coding standards and includes appropriate tests.
