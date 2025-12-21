# Modified Containerized GPU Inference Image For Vertex AI Deployment

FROM nvidia/cuda:11.8.0-base-ubuntu22.04

ENV DEBIAN_FRONTEND=noninteractive \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    CUDA_VISIBLE_DEVICES=all \
    NVIDIA_VISIBLE_DEVICES=all \
    NVIDIA_DRIVER_CAPABILITIES=compute,utility

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    python3.10 python3-pip python3.10-dev \
    ffmpeg git libsndfile1 libasound2-dev \
    curl ca-certificates \
    && rm -rf /var/lib/apt/lists/* /var/cache/apt/archives/*

# Set python aliases
RUN ln -sf /usr/bin/python3.10 /usr/bin/python && \
    ln -sf /usr/bin/pip3 /usr/bin/pip

WORKDIR /app

# Upgrade pip and install torch
RUN pip install --upgrade pip setuptools wheel && \
    pip install --no-cache-dir \
        torch==2.0.1+cu118 \
        torchvision==0.15.2+cu118 \
        torchaudio==2.0.2+cu118 \
    --extra-index-url https://download.pytorch.org/whl/cu118

# Install UVR directly from GitHub
RUN pip install --no-cache-dir git+https://github.com/NextAudioGen/ultimatevocalremover_api.git@main#egg=uvr

# Install remaining requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy FastAPI app
COPY main_ikenna.py .

# Runtime directories
RUN mkdir -p /tmp && chmod 777 /tmp

# Cleanup pip cache
RUN pip cache purge

# Add health check for GPU
HEALTHCHECK --interval=30s --timeout=10s --start-period=60s --retries=3 \
    CMD python -c "import torch; exit(0 if torch.cuda.is_available() else 1)"

# Expose app port
EXPOSE 8000

# Start FastAPI with Uvicorn
CMD ["uvicorn", "main_ikenna:app", "--host", "0.0.0.0", "--port", "8000"]
