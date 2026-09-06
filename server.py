"""
FastAPI Server for 90-Class Animal Classifier & Speech API.
Serves the interactive web interface and provides the /api/predict REST endpoint.
"""

import os
import sys
import io
import json
import numpy as np
from PIL import Image
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from animal_data import get_animal_info

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

app = FastAPI(title="Animal Vision & Speech API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def add_private_network_headers(request, call_next):
    response = await call_next(request)
    response.headers["Access-Control-Allow-Private-Network"] = "true"
    return response

# Global model and classes
MODEL = None
CLASSES = []


def load_classes():
    classes_path = os.path.join(os.path.dirname(__file__), "classes.json")
    if os.path.exists(classes_path):
        with open(classes_path, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def get_model():
    global MODEL
    if MODEL is None:
        import tensorflow as tf
        candidates = [
            os.path.join(os.path.dirname(__file__), "animal_model.keras"),
            os.path.join(os.path.dirname(__file__), "best_animal_model.keras")
        ]
        model_path = None
        for cand in candidates:
            if os.path.exists(cand):
                model_path = cand
                break

        if not model_path:
            raise FileNotFoundError("Model file animal_model.keras not found. Please run train.py first.")
        
        print(f"Loading model from {model_path}...")
        MODEL = tf.keras.models.load_model(model_path)
    return MODEL


@app.on_event("startup")
def startup_event():
    global CLASSES
    CLASSES = load_classes()
    try:
        get_model()
        print("✅ Animal model loaded successfully on startup.")
    except Exception as e:
        print(f"⚠️ Model load deferred or error: {e}")


async def process_prediction(upload_file: UploadFile):
    model = get_model()
    contents = await upload_file.read()
    image = Image.open(io.BytesIO(contents)).convert("RGB")
    resized = image.resize((300, 300))
    img_array = np.array(resized, dtype=np.float32)
    img_batch = np.expand_dims(img_array, axis=0)

    predictions = model.predict(img_batch, verbose=0)[0]
    best_idx = int(np.argmax(predictions))
    best_animal = CLASSES[best_idx]
    best_confidence = float(predictions[best_idx] * 100)

    top_5_indices = np.argsort(predictions)[-5:][::-1]
    top_5 = [
        {
            "rank": r,
            "animal": CLASSES[idx].title(),
            "confidence": round(float(predictions[idx] * 100), 2)
        }
        for r, idx in enumerate(top_5_indices, 1)
    ]

    if best_confidence >= 80:
        tier = "High Confidence"
        tier_message = f"High confidence: This animal is most likely a {best_animal.title()}."
    elif best_confidence >= 50:
        tier = "Medium Confidence"
        tier_message = f"Medium confidence: The animal may be a {best_animal.title()}."
    else:
        tier = "Low Confidence"
        tier_message = f"Low confidence prediction. Best guess: {best_animal.title()}."

    info = get_animal_info(best_animal)

    return {
        "success": True,
        "animal": best_animal.title(),
        "predicted_animal": best_animal,
        "confidence": round(best_confidence, 2),
        "confidence_formatted": f"{best_confidence:.2f}%",
        "confidence_level": tier,
        "tier": tier,
        "tier_message": tier_message,
        "top_5": top_5,
        "info": info
    }


@app.post("/predict")
@app.post("/api/predict")
async def predict_endpoint(file: UploadFile = File(None), image: UploadFile = File(None)):
    target_file = file or image
    if not target_file:
        raise HTTPException(status_code=400, detail="No file uploaded. Please upload a file via 'file' or 'image' field in multipart/form-data.")
    try:
        result = await process_prediction(target_file)
        return JSONResponse(result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/classes")
def list_classes():
    return {"classes": CLASSES, "total": len(CLASSES)}


# Mount static web assets
web_dir = os.path.join(os.path.dirname(__file__), "web")
if os.path.exists(web_dir):
    app.mount("/", StaticFiles(directory=web_dir, html=True), name="web")


if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
