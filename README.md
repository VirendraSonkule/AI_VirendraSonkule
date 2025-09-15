# AI-Powered Educational Video Automation System

## Project Overview

This project automates the creation of high-quality educational videos using Artificial Intelligence and the Manim animation engine. Students can request detailed explanations of specific concepts from various knowledge domains, such as GIS, Space Technology, and Data Structures & Algorithms. The system:

- Uses a **Knowledge Graph** built from domain-specific books and resources.
- Leverages **Natural Language Processing (NLP)** and **Large Language Models (LLMs)** to generate detailed, structured educational scripts.
- Converts scripts into animated slides using **Manim**, an open-source mathematical animation engine.
- Compiles animations into complete educational videos, optionally adding voiceover and background music.

This system aims to democratize learning by creating customized educational content on-demand.

---

## Features

- **Intelligent Query Understanding:** Extracts user intent and concept from natural language queries.
- **Knowledge Graph Integration:** Retrieves structured knowledge to ensure accurate and comprehensive explanations.
- **Automated Script Generation:** Uses GPT-4 or other LLMs to produce detailed, easy-to-understand scripts.
- **Dynamic Animation Generation:** Converts scripts into visually engaging Manim animations.
- **Multi-Domain Support:** Includes specialized modules for GIS, Space Technology, and Data Structures & Algorithms.
- **End-to-End Pipeline:** From user query to downloadable educational video.
- **Extensible & Modular:** Easily add new domains, animation templates, or NLP improvements.

---

## Tech Stack

| Layer                   | Technology / Framework                      | Purpose                                                  |
|-------------------------|--------------------------------------------|----------------------------------------------------------|
| **Frontend / UI**       | Streamlit / Flask / React                   | Web interface for student interaction                    |
| **NLP & Language Models**| OpenAI GPT-4, Hugging Face Transformers    | Query understanding, script generation                   |
| **Knowledge Graph**      | Neo4j / NetworkX / RDF + SPARQL             | Store and query structured knowledge                      |
| **Backend**              | Python 3.9+                                | Core orchestration and APIs                               |
| **Animation Engine**     | [Manim Community Edition](https://docs.manim.community/en/stable/) | Generate mathematical and educational animations          |
| **Text-to-Speech (TTS)**| ElevenLabs, Coqui TTS, Google Text-to-Speech API | Convert scripts into voiceovers                            |
| **Video Processing**     | MoviePy, FFmpeg                            | Compile scenes, merge audio and video                     |
| **Cloud / Deployment**   | Docker, AWS / GCP / Heroku                  | Containerization and deployment                           |
| **Data Storage**         | PostgreSQL / MongoDB / File System          | Store scripts, user queries, video assets                 |
| **Monitoring & Logging** | Prometheus, ELK Stack                       | System health and debugging                               |

---

## Architecture Overview


User Query --> NLP Module --> Knowledge Graph Query --> Script Generation (LLM) --> Slide Generation --> Manim Animation --> Video Compilation --> Output Delivery

## Folder Structure
---
prototype/
├── manim_renderer.py
├── script_generator.py
├── main.py
├── requirements.txt
└── .env
---



## Extending the System

Add new domains: Populate the knowledge graph with books/data for new fields.

Improve NLP models: Train custom NLU models for better query understanding.

Enhance animations: Create domain-specific Manim templates with rich visuals.

Add voiceovers: Integrate TTS services for natural-sounding narration.

Deploy at scale: Use Kubernetes/Docker for scalable, multi-user access.


## Installation

## Prerequisites

Python 3.9 or higher

Manim Community Edition installed (Installation Guide
)

OpenAI API Key (or equivalent LLM API)

FFmpeg installed (for video compilation)

(Optional) Docker

## Clone the repository
git clone https://github.com/yourusername/Educational-Video-Automation.git
cd Educational-Video-Automation

## Install dependencies
pip install -r requirements.txt

## Set environment variables

Create a .env file in the root directory:

OPENAI_API_KEY=your_openai_api_key_here
TTS_API_KEY=your_tts_api_key_here  # if using TTS service

## Usage
Running the Web Application

Start the Streamlit or Flask web app:

streamlit run webapp/app.py
 or
python webapp/app.py

## Querying Concepts

Enter your educational query in the web interface, such as:

"Explain Binary Search Trees in Data Structures"

"What is Geographic Information System (GIS)?"

"Describe orbital mechanics in Space Technology"

The system will generate and display an animated educational video explaining the concept.

CLI (Prototype)

Alternatively, run the prototype CLI:

python main.py


Enter the concept, and the system will:

Generate a detailed script using GPT-4

Convert it into slides

Render Manim animations

Produce a video output


## License

This project is licensed under the MIT License
