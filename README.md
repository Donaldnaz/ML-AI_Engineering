
# Azure-Powered Computer Vision: Automated Image Analysis & Object Detection

## Project Overview
Built an AI-powered image analysis tool using Azure Vision APIs to automate structured insight extraction from images — reducing manual tagging and accelerating decision-making across visual data workflows.

### Problem Statement
Working with raw image data locally often results in:
- Manual tagging and annotation that doesn't scale
- Limited access to advanced computer vision without complex setups
- Risk of inconsistent results using offline tools
- Slow workflows that delay insight extraction

### Project Goal
Create a lightweight, reproducible tool that users can use to:
- Analyze images using pre-trained models
- Perform OCR to read text from images
- Detect and recognize human faces and emotions
- Train custom models for image classification and object detection
- Analyze video content and generate AI-powered insights
- Build applications with vision-enabled generative AI

## Tech Stack
| Component | Tools Used |
|-----------|------------|
| **Programming** | Python 3.10 |
| **SDK/API** | Azure AI Vision SDK (`azure-ai-vision-imagenalysis`) |
| **Image Handling** | Pillow (PIL), Matplotlib |
| **Security** | dotenv for credentials management |
| **Output Formats** | Visual overlays (.jpg), structured logs (stdout), JSON |

## Key Features

### **A) Face Detection, Analysis and Recognition**
Built applications that detect human faces, analyze facial attributes, and recognize individuals using Azure's AI Vision Face API.

**Applications:**
- Identity verification systems (KYC)
- Face unlock and personalized user experiences
- Surveillance and access control in smart buildings
- Retail customer sentiment analysis

**Capabilities:**
- Face detection with bounding boxes
- Attribute analysis (age, emotion, pose)
- Face verification & identification
- Facial landmarks detection (eyes, nose, mouth)
- Privacy-aware, Responsible AI ready

### **B) Image Classification with Custom Vision**
Train custom models to classify images into specific categories with high accuracy using few images.

**Applications:**
- Retail: Automatically tagging products for inventory management
- Agriculture: Identifying plant diseases or animal breeds
- Construction: Classifying safety gear in site photos
- Healthcare: Recognizing medical conditions (with regulatory guidance)

**Capabilities:**
- Custom classifier training
- High accuracy with few images
- Easy retraining & versioning
- Export to edge or cloud
- API + UI integration

### **C) Object Detection in Images**
Develop models that detect and localize multiple objects within a single image.

**Applications:**
- Retail Loss Prevention: Spot concealed items at checkout
- Smart Construction Monitoring: Detect missing safety gear
- Warehouse Automation: Track inventory movement
- Traffic Management: Identify license plates, vehicle counts

## Real-World Use Case: Smart Access Control System

### **Architecture:**

<img width="427" height="240" alt="image" src="https://github.com/user-attachments/assets/febfc053-bcf9-4a41-8979-48eef58a398f" />

### **What It Does:**
1. Detects and identifies faces from camera feeds
2. Matches against a list of approved personnel
3. Flags unknown individuals for security review
4. Stores and indexes video footage for audit trails

### **Business Impact:**
- Faster and smarter entry process for authorized staff
- Reduced risk of unauthorized access
- Audit-ready, searchable video logs
- Enhanced security using AI-powered surveillance

## Project Outcomes
- Built cloud-native tools for image tagging, OCR, face detection & object recognition
- Trained and tested custom classification models via Azure Custom Vision
- Extracted insights from video: face tracking, speech-to-text, scene segmentation
- Wrote modular Python scripts using Azure SDKs, dotenv, and PIL
- Produced visual and structured outputs (image overlays, logs, JSON)
- Secured credentials and APIs via environment variable handling

## Next Steps
- Wrap modules into a deployable Streamlit or FastAPI demo
- Host application using Azure App Service or Container Apps
- Automate image processing with Azure Functions + Blob Triggers
- Benchmark Azure Computer Vision vs. AWS Rekognition & Google Vision AI

## 📁 Project Structure
```
computer-vision/
├── src/
│   ├── face_analysis/
│   │   └── analyze-faces.py
│   ├── image_classification/
│   │   ├── train.py
│   │   └── classifier.py
│   └── object_detection/
│       ├── train-detector.py
│       └── test-detector.py
├── images/              # Training and test images
├── .env.example         # Environment variables template
├── requirements.txt     # Python dependencies
└── README.md            # This file
```

## Getting Started
1. **Prerequisites:**
   - Azure account with Computer Vision and Custom Vision services
   - Python 3.10+
   - Azure CLI installed

2. **Setup:**
```bash
# Clone repository
git clone <repository-url>

# Install dependencies
pip install -r requirements.txt

# Configure environment variables
cp .env.example .env
# Add your Azure credentials to .env
```

3. **Run Face Detection:**
```bash
python src/face_analysis/analyze-faces.py images/face1.jpg
```


## Authored By
## Anasieze Ikenna - Cloud & AI Solutions Engineer
