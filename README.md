```markdown
# 🧠 Nail Detection & Measurement System

An end-to-end system to **detect nails**, **measure their size**, **estimate weight**, and **generate human-readable reports** using a trained **YOLOv8** model and **OpenAI GPT**.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![YOLOv8](https://img.shields.io/badge/YOLO-v8-brightgreen)
![FastAPI](https://img.shields.io/badge/FastAPI-🚀-green)
![OpenAI GPT](https://img.shields.io/badge/OpenAI-GPT3.5-ff69b4)
![License](https://img.shields.io/github/license/your-username/nail-detector)

---

## 🔧 Features

- 🧠 **YOLOv8 Training**: Prepares and trains a custom YOLOv8 model on nail image datasets.
- 📐 **Measurement Engine**: Converts bounding boxes into **real-world mm dimensions** using calibration data.
- ⚖️ **Weight Estimation**: Calculates the estimated **weight in grams** using a specified material density.
- 🖼️ **Annotated Output**: Saves images with **bounding boxes** around detected nails.
- 🧾 **LLM Reporting**: Generates **natural language summaries** of measurements using GPT-3.5 Turbo.
- 🌐 **FastAPI Web Service**: Upload and process images via an easy-to-use REST API.

---

## 🧱 Tech Stack

| Tool           | Use                                           |
|----------------|-----------------------------------------------|
| Python 3.8+    | Programming Language                          |
| YOLOv8         | Nail detection model                          |
| OpenCV + NumPy | Image processing & numerical computation      |
| FastAPI        | Web service / API backend                     |
| OpenAI GPT-3.5 | LLM-based report generation                   |
| PyYAML, Pathlib| Config and file handling                      |

---

## 📁 Project Structure

```

.
├── main.py              # FastAPI API server
├── test.py              # Training pipeline
├── test\_script.py       # Inference & measurement logic
├── llm\_helper.py        # GPT-based report generator
├── data\_fixed.yaml      # Auto-generated data config
├── requirements.txt     # Python dependencies
└── Nail\_dataset/        # Dataset folder

````

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/nail-detector.git
cd nail-detector
````

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Train the YOLO Model

```bash
python test.py
```

This will:

* Fix dataset paths
* Start training using YOLOv8
* Save the best model as `nail_detector.pt`

---

## 🔍 Run Detection & Measurement

```python
from test_script import detect_and_measure

results, output_path = detect_and_measure("sample.jpg")
print(results)
```

Returns:

* Bounding boxes
* Heights in mm
* Weights in grams
* Annotated image saved locally

---

## 🌐 Run FastAPI Web Server

```bash
uvicorn main:app --reload
```

### API Endpoint: `/upload-image`

**Method**: `POST`
**Form field**: `file` (image file)
**Returns**:

```json
{
  "measurements": [...],
  "report": "Detected 4 nails. Average height is..."
}
```

---

## 📸 Example Output

> “Detected 4 nails with an average height of 35.6 mm and average weight of 4.7 grams…”

![output\_image\_sample](example_output.jpg)

---

## 📄 License

This project is licensed under the MIT License.

---

## 🙌 Acknowledgements

* Ultralytics YOLOv8 for object detection
* OpenAI for GPT-3.5 API
* FastAPI for lightweight API deployment

---
