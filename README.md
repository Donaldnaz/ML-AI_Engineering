# **Deployed Audio-Processing Model with GPU Acceleration on Vertex AI**

This project demonstrates how I containerized and deployed an audio processing model built with Docker and deployed to a Vertex AI endpoint. The solution uses GPU acceleration for low-latency inference and is designed for scalable, real-time audio processing using custom containers fully compatible with Vertex AI.

The model is an intelligent media processing service that takes in video or audio files from Google Cloud Storage (GCS), separates vocals from instrumentals using deep learning (UVR), and outputs:

•	Clean vocal tracks

•	Isolated instrumentals

•	Video with no audio

# **Tech Stack**

•	Google Cloud Vertex AI (Custom Model Deployment)

•	NVIDIA CUDA + Tesla T4 GPU

•	Docker (Multi-stage build, CUDA support)

•	FastAPI (Custom endpoints: /, /health, /read)

•	PyTorch, Whisper, PyAnnote.audio

•	Cloud Storage (GCS Buckets for model I/O)


## Project Structure

````
├── Architecture.png                      # Architecture Diagram
├── Guide.pdf                             # Step by Step Deployment Guide
├── Dockerfile                            # Containerized GPU Inference Image
├── main.py                               # FastAPI Inference Service for Vertex AI
├── README.md                             # Project Overview 

````

### **Project Highlights**

This project taught me how to take an AI model from experimentation to production, using cloud infrastructure, GPUs, and MLOps practices to build a scalable, reliable, and observable AI service.

### Author
### Anasieze Ikenna - Cloud Engineer
