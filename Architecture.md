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
