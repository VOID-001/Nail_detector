# 🧠 Nail Detection & Measurement System using YOLOv8 + LLM Reports

This project provides a complete end-to-end solution for detecting nails in images, measuring their dimensions, estimating weight, and generating detailed natural-language reports — all powered by YOLOv8, OpenCV, FastAPI, and OpenAI's GPT.

## 🚀 Features

* 🔍 **YOLOv8 Model Training**: Custom training pipeline for detecting nails using Ultralytics YOLO
* 📏 **Automated Measurement**: Converts bounding box pixel dimensions into real-world units (mm), with weight estimation
* 🖼️ **Annotated Output**: Saves annotated images highlighting detected nails with bounding boxes
* 🧾 **LLM-Powered Reports**: Converts raw measurements into easy-to-understand summaries using GPT-3.5
* 🌐 **FastAPI Web Service**: Upload images via an API endpoint and get structured JSON results with visuals and reports

## 🛠️ Tech Stack

* Python 3.8+
* Ultralytics YOLOv8
* OpenCV & NumPy
* FastAPI + Uvicorn
* OpenAI GPT-3.5 API
* PyYAML, pathlib, os

## 📁 Project Structure

```
.
├── main.py                 # FastAPI entry point
├── Training.py                 # YOLO training and config fixer
├── test_script.py          # Image detection & measurement
├── llm_helper.py           # Converts measurements to report using GPT
├── data_fixed.yaml         # Auto-generated fixed dataset paths
├── Nail_dataset/           # Training/validation/test data
│   ├── train/
│   ├── valid/
│   └── test/
├── runs/                   # YOLOv8 training outputs
├── annotated_images/       # Output images with detections
└── requirements.txt        # Python dependencies
```

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- CUDA-compatible GPU (recommended for training)

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd nail-detection-system
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Set up OpenAI API Key
Create a `.env` file in the project root:
```bash
OPENAI_API_KEY=your_openai_api_key_here
```

## 📦 How to Use

### 1. Train the Model
```bash
python Training.py
```
This will:
- Fix dataset configuration paths
- Start YOLOv8 training process
- Save the trained model in `runs/detect/train/weights/`

### 2. Run Detection and Get Measurements
```python
from test_script import detect_and_measure

# Detect nails in an image and get measurements
result = detect_and_measure("sample.jpg")
print(result)
```

### 3. Start the Web Service
```bash
uvicorn main:app --reload
```
The API will be available at `http://localhost:8000`

#### API Endpoints:
- `POST /detect/`: Upload an image file to detect nails
- `GET /docs`: Interactive API documentation

### 4. Using the API
```python
import requests

# Upload image for detection
with open("nail_image.jpg", "rb") as f:
    response = requests.post("http://localhost:8000/detect/", files={"file": f})
    
result = response.json()
print(result)
```

## 📊 Output Format

The system returns structured data including:

```json
{
  "detections": [
    {
      "nail_id": 1,
      "confidence": 0.95,
      "dimensions": {
        "length_mm": 45.2,
        "width_mm": 3.1,
        "estimated_weight_g": 2.8
      },
      "bounding_box": [x1, y1, x2, y2]
    }
  ],
  "summary": {
    "total_nails": 3,
    "total_weight_g": 8.4
  },
  "llm_report": "Detailed natural language analysis...",
  "annotated_image_path": "annotated_images/output_001.jpg"
}
```

## 🔧 Configuration

### Model Parameters
Edit the training parameters in `test.py`:
```python
model.train(
    data='data_fixed.yaml',
    epochs=100,
    imgsz=640,
    batch=16
)
```

### Measurement Calibration
Adjust the pixel-to-mm conversion factor in `test_script.py`:
```python
PIXELS_PER_MM = 10.5  # Calibrate based on your images
```

## 📸 Sample Results

The system generates annotated images showing:
- Bounding boxes around detected nails
- Confidence scores
- Dimension measurements
- Unique nail IDs

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🐛 Troubleshooting

### Common Issues:

1. **CUDA Out of Memory**: Reduce batch size in training configuration
2. **OpenAI API Errors**: Check your API key and usage limits
3. **Model Not Found**: Ensure training completed successfully and model exists in `runs/detect/train/weights/`

### Support

For issues and questions, please open an issue on GitHub or contact the development team.

---

**Built with ❤️ using YOLOv8 and FastAPI**
