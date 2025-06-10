import cv2, numpy as np
from ultralytics import YOLO

class NailTester:
    def __init__(self, model_path="nail_detector.pt", calib=0.1, density=7.8):
        self.model = YOLO(model_path)
        self.p2mm  = calib
        self.density = density

    def detect_and_measure(self, img_path):
        img = cv2.imread(img_path)
        boxes = self.model(img, conf=0.25)[0].boxes.xyxy.cpu().numpy().astype(int)
        meas=[]
        for x1,y1,x2,y2 in boxes:
            h_px=x2-x1 if (x2-x1)>(y2-y1) else y2-y1
            h_mm = h_px * self.p2mm
            w_g  = h_mm * self.density
            meas.append({"bbox":[x1,y1,x2,y2],"height_mm":round(h_mm,1),"weight_g":round(w_g,2)})
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
        out = img_path.replace(".", "_out.")
        cv2.imwrite(out, img)
        return meas, out

def detect_and_measure(path):
    return NailTester().detect_and_measure(path)
