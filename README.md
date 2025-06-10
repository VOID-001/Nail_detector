```markdown
# Nail Detection & Measurement System

An intelligent system to **detect nails**, **measure their dimensions**, **estimate their weight**, and generate **concise reports** — powered by **YOLOv8**, **OpenCV**, and **OpenAI GPT**.

---

## 🔍 Overview

This project combines deep learning and computer vision with a lightweight API backend to deliver an automated nail measurement pipeline. It allows you to:

- Train a YOLOv8 model on custom nail datasets.
- Automatically detect and measure nails in images.
- Estimate weight using physical density.
- Generate descriptive reports using GPT.
- Host an API using FastAPI for on-demand predictions.

---

## ⚙️ Features

- **Custom Object Detection** — Train YOLOv8 on your nail dataset.
- **Measurement Engine** — Convert bounding boxes into real-world mm values.
- **Weight Calculation** — Estimate weights using material density.
- **Annotated Output** — Save images with visual bounding boxes.
- **LLM Reporting** — Auto-generate readable reports using OpenAI GPT-3.5.
- **Web API** — Upload images and get predictions via a REST API.

---

## 🧱 Tech Stack

| Technology     | Purpose                            |
|----------------|-------------------------------------|
| Python 3.8+     | Core language                     |
| YOLOv8          | Nail detection                    |
| OpenCV & NumPy  | Image processing & math utilities |
| FastAPI         | REST API server                   |
| OpenAI GPT-3.5  | Report generation                 |
| PyYAML, Pathlib | Configuration & file handling     |

---

## 📁 Folder Structure

```

.
├── main.py              # FastAPI API server
├── test.py              # Training logic
├── test\_script.py       # Detection and measurement engine
├── llm\_helper.py        # GPT-based report generation
├── data\_fixed.yaml      # Configured dataset YAML
├── requirements.txt     # Dependencies
├── Nail\_dataset/        # Dataset directory

````

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/nail-detector.git
cd nail-detector
````

### 2. Install Requirements

```bash
pip install -r requirements.txt
```

### 3. Train the Model

```bash
python test.py
```

This script:

* Fixes the dataset YAML paths
* Trains the model
* Saves the best weights to `nail_detector.pt`

---

## 🧪 Run Detection & Measurement

```python
from test_script import detect_and_measure

measurements, image_path = detect_and_measure("sample.jpg")
print(measurements)
```

> ✅ Output includes: nail dimensions (in mm), estimated weight (g), and an annotated image.

---

## 🌐 API Usage

Start the API:

```bash
uvicorn main:app --reload
```

Upload an image using `/upload-image` endpoint (`POST` request with image in `file` form field).

**Response:**

```json
{
  "measurements": [...],
  "report": "Detected 3 nails. Average height is 42 mm..."
}
```

---

## 📷 Sample Output

![Sample Output](example_output.jpg)

---

## 📄 License

This project is licensed under the MIT License.

---

## 🙌 Acknowledgements

* [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)
* [OpenAI](https://openai.com)
* [FastAPI](https://fastapi.tiangolo.com/)

---

```
