# Deployed Audio-Processing Model with GPU Acceleration on Vertex AI

This project demonstrates how I containerized and deployed an audio processing model built with Docker and deployed to a Vertex AI endpoint. The solution uses GPU acceleration for low-latency inference and is designed for scalable, real-time audio processing using custom containers fully compatible with Vertex AI.

The model is an intelligent media processing service that takes in video or audio files from Google Cloud Storage (GCS), separates vocals from instrumentals using deep learning (UVR), and outputs:
•	Clean vocal tracks
•	Isolated instrumentals
•	Video with no audio

### Tech Stack
•	Google Cloud Vertex AI (Custom Model Deployment)
•	NVIDIA CUDA + Tesla T4 GPU
•	Docker (Multi-stage build, CUDA support)
•	FastAPI (Custom endpoints: /, /health, /read)
•	PyTorch, Whisper, PyAnnote.audio
•	Cloud Storage (GCS Buckets for model I/O)


## Project Structure

````
/src                                      # Project Source Directory
├── Architecture.png                      # Cloud Architecture Diagram
├── Guide.pdf                             # Step by Step Deployment Guide
├── Prerequisites.md                      # Prerequisites to Deploy Stack
├── README.md                             # Project Overview 

````


<img width="468" height="211" alt="image" src="https://github.com/user-attachments/assets/f9b1c732-5663-4eb3-ab48-ce9d9367aae9" />

- **Develop Natural Language Solutions.** → [`NLP`](https://anasiezeikenna.notion.site/Develop-Natural-Language-Solutions-in-Azure-27105c74585e8055bbabde6e9d5894fd)

- **Develop Natural Language Solutions.** → [`Computer Vision`](https://anasiezeikenna.notion.site/Developing-Computer-Vision-Solutions-in-Azure-24505c74585e81d2af8fe4d90ff7260f)  

- **Develop Generative AI Solutions.** → [`Generative AI`](https://anasiezeikenna.notion.site/Developing-Generative-AI-Solutions-26005c74585e804b98e3ceebe191f827)
