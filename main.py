import shutil
from pathlib import Path
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse, HTMLResponse
from test_script import detect_and_measure
from llm_helper import summarize_measurements

PROJECT_NAME = "🔨 Hammer_of_Thor"
VERSION = "v1.0"
ROOT = Path(__file__).parent
OUTPUT_DIR = ROOT / "static" / "outputs"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

app = FastAPI(
    title=PROJECT_NAME,
    version=VERSION,
    description="Upload an image of nails; get back measurements & a polished report."
)

@app.get("/", response_class=HTMLResponse)
async def docs_page():
    return f"""
    <html>
      <head><title>{PROJECT_NAME}</title></head>
      <body>
        <h1>{PROJECT_NAME}</h1>
        <p>Version: {VERSION}</p>
        <p>Use <code>POST /detect</code> with an image file to get nail measurements.</p>
      </body>
    </html>
    """

@app.post("/Detection", summary="Detect & Measure Nails")
async def detect(file: UploadFile = File(...)):
    # 1) Validate and save upload
    if not file.content_type.startswith("image/"):
        raise HTTPException(400, "Only image files are accepted.")
    upload_path = OUTPUT_DIR / file.filename
    with open(upload_path, "wb") as f:
        f.write(await file.read())

    # 2) Run detection + measurement
    raw_meas, annotated_img = detect_and_measure(str(upload_path))

    # 3) Save annotated image (skip if same)
    dest = OUTPUT_DIR / (upload_path.stem + "_out" + upload_path.suffix)
    if Path(annotated_img).resolve() != dest.resolve():
        shutil.copy(annotated_img, dest)

    # 4) Convert measurements to Python types
    measurements = []
    for m in raw_meas:
        measurements.append({
            "bbox": [int(v) for v in m["bbox"]],
            "height_mm": float(m["height_mm"]),
            "weight_g":  float(m["weight_g"])
        })

    # 5) LLM summary
    report = summarize_measurements(measurements, file.filename)

    # 6) Return only text data
    return JSONResponse({
        "measurements": measurements,
        "report":       report
    })

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
