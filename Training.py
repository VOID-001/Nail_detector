import os
import yaml
from pathlib import Path
from ultralytics import YOLO

# ── CONFIG ───────────────────────────────────────────────────────────────
ROOT           = Path(__file__).parent
DATASET_ROOT   = ROOT / "Nail_dataset"
DATA_YAML      = DATASET_ROOT / "data.yaml"
FIXED_YAML     = ROOT / "data_fixed.yaml"
MODEL_WEIGHTS  = ROOT / "yolov8n.pt"
OUTPUT_MODEL   = ROOT / "nail_detector.pt"

# ── FIX DATA.YAML PATHS ────────────────────────────────────────────────────
def fix_yaml():
    with open(DATA_YAML, "r") as f:
        cfg = yaml.safe_load(f)

    # Overwrite train/val/test to point to images subfolders
    cfg["train"] = str(DATASET_ROOT / "train" / "images")
    cfg["val"]   = str(DATASET_ROOT / "valid" / "images")
    if (DATASET_ROOT / "test" / "images").exists():
        cfg["test"] = str(DATASET_ROOT / "test" / "images")
    # Ensure nc matches names
    names = cfg.get("names", [])
    cfg["nc"] = len(names)

    with open(FIXED_YAML, "w") as f:
        yaml.dump(cfg, f, sort_keys=False)

    print(f"✔️  data_fixed.yaml written with corrected paths")
    return FIXED_YAML

# ── TRAIN MODEL ───────────────────────────────────────────────────────────
def train_model(yaml_path: Path, epochs=50, imgsz=640, batch=8):
    print("Starting YOLOv8 training for nail detection")
    model = YOLO(str(MODEL_WEIGHTS))
    model.train(
        data=str(yaml_path),
        epochs=epochs,
        imgsz=imgsz,
        batch=batch,
        project=str(ROOT),
        name="nail_detector",
        exist_ok=True
    )
    best = ROOT / "nail_detector" / "weights" / "best.pt"
    if best.exists():
        os.replace(str(best), str(OUTPUT_MODEL))
        print(f" Model saved to {OUTPUT_MODEL}")
    else:
        print(" best.pt not found - did training succeed?")

# ── MAIN ──────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    fixed = fix_yaml()
    train_model(fixed)
