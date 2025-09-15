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

```plaintext
User Query --> NLP Module --> Knowledge Graph Query --> Script Generation (LLM) --> Slide Generation --> Manim Animation --> Video Compilation --> Output Delivery



Extending the System

Add new domains: Populate the knowledge graph with books/data for new fields.

Improve NLP models: Train custom NLU models for better query understanding.

Enhance animations: Create domain-specific Manim templates with rich visuals.

Add voiceovers: Integrate TTS services for natural-sounding narration.

Deploy at scale: Use Kubernetes/Docker for scalable, multi-user access.


