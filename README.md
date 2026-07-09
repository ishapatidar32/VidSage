# VidSage 🎯
### Semantic Video Search Engine powered by RAG

## 🚀 What is VidSage?
VidSage is an end-to-end AI pipeline that converts 
video content into an intelligent search engine. 
Instead of scrubbing through hours of video, simply 
ask a question and get the exact timestamp and answer 
instantly.

## 🎯 Problem it Solves
Finding specific information in long videos is painful 
and time-consuming. VidSage solves this by converting 
video speech into searchable knowledge using 
state-of-the-art AI — completely free, no paid APIs.

## ⚙️ How it Works
Video/Audio
↓
Whisper STT (Speech to Text)
↓
spaCy (Text Cleaning + Keywords)
↓
Sentence Embeddings (nomic-embed-text)
↓
ChromaDB (Vector Storage)
↓
RAG Pipeline (LangChain + Ollama)
↓
Answer with Timestamp
## 🛠️ Tech Stack
| Layer | Technology |
|---|---|
| Speech to Text | OpenAI Whisper |
| Text Processing | spaCy |
| Embeddings | nomic-embed-text (Ollama) |
| Vector Database | ChromaDB |
| RAG Pipeline | LangChain |
| Local LLM | LLaMA 3.1 (Ollama) |
| API | FastAPI |
| UI | Streamlit |

## ✨ Key Features
- 🎙️ Automatic speech to text (supports Hindi → English)
- 🔍 Semantic search across multiple videos
- ⏱️ Exact timestamp retrieval
- 🆓 100% free — runs completely on local system
- 📦 No paid APIs required
- 🚀 Works with any video content

## 🏃 Quick Start
```bash
# Clone repo
git clone https://github.com/yourusername/vidsage

# Create virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run pipeline
python pipeline.py

# Start UI
streamlit run app.py
```

## 📁 Project Structure
vidsage/
├── audios_trimmed/     ← processed audio files
├── transcripts/        ← whisper output JSON
├── processed/          ← spaCy cleaned chunks
├── embeddings/         ← vector embeddings
├── stt.py              ← speech to text pipeline
├── process.py          ← text processing
├── embed.py            ← embedding generation
├── rag.py              ← RAG pipeline
├── api.py              ← FastAPI backend
├── app.py              ← Streamlit UI
└── requirements.txt    ← dependencies

## 🎯 Use Cases
- Search specific topics in online course videos
- Find information in YouTube tutorials
- Query lecture recordings
- Search corporate training videos

## 👨‍💻 Built By
[Your Name] — Placement Project 2026
