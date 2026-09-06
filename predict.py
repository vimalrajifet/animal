"""
Animal Prediction & Inference CLI
Predict animal classes and confidence scores using the trained EfficientNetB3 model.
"""

import os
import sys
import argparse
import json

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

import numpy as np
from PIL import Image


def load_classes(classes_path=None):
    if not classes_path or not os.path.exists(classes_path):
        classes_path = os.path.join(os.path.dirname(__file__), "classes.json")
    
    if os.path.exists(classes_path):
        with open(classes_path, "r", encoding="utf-8") as f:
            return json.load(f)
    
    # Fallback to reading name of the animals.txt
    txt_path = os.path.join(os.path.dirname(__file__), "archive", "name of the animals.txt")
    if os.path.exists(txt_path):
        with open(txt_path, "r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip()]
            
    raise FileNotFoundError("Could not find classes.json or name of the animals.txt.")


def predict_image(image_path, model_path="best_animal_model.keras", img_size=300):
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image not found at: {image_path}")
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found at: {model_path}. Please train the model first.")

    import tensorflow as tf

    classes = load_classes()
    model = tf.keras.models.load_model(model_path)

    # 1. Load and resize
    raw_img = Image.open(image_path).convert("RGB")
    resized_img = raw_img.resize((img_size, img_size))

    # 2. Convert to numpy array & expand dims
    img_array = np.array(resized_img, dtype=np.float32)
    img_batch = np.expand_dims(img_array, axis=0)

    # 3. Model inference
    predictions = model.predict(img_batch, verbose=0)[0]

    # Top prediction
    best_idx = int(np.argmax(predictions))
    best_animal = classes[best_idx]
    best_confidence = float(predictions[best_idx] * 100)

    # Top 5 predictions
    top_5_indices = np.argsort(predictions)[-5:][::-1]
    top_5 = [
        {
            "rank": rank,
            "animal": classes[idx],
            "confidence": float(predictions[idx] * 100)
        }
        for rank, idx in enumerate(top_5_indices, start=1)
    ]

    # Confidence tier
    if best_confidence >= 80:
        tier = "High Confidence"
        tier_message = f"High confidence: This animal is most likely a {best_animal.title()}."
    elif best_confidence >= 50:
        tier = "Medium Confidence"
        tier_message = f"Medium confidence: The animal may be a {best_animal.title()}."
    else:
        tier = "Low Confidence"
        tier_message = f"Low confidence prediction. Best guess: {best_animal.title()}."

    return {
        "image_path": image_path,
        "predicted_animal": best_animal,
        "confidence": best_confidence,
        "top_5": top_5,
        "tier": tier,
        "tier_message": tier_message,
        "all_probabilities": predictions
    }


def main():
    parser = argparse.ArgumentParser(description="Predict animal from image")
    parser.add_argument("image_path", type=str, nargs="?", default=None, help="Path to input image")
    parser.add_argument("--model", type=str, default="best_animal_model.keras", help="Path to trained model")
    parser.add_argument("--img_size", type=int, default=300, help="Image size (default 300)")
    parser.add_argument("--sample", type=str, default=None, help="Animal name to pick a random test image from archive")
    args = parser.parse_args()

    image_path = args.image_path

    # If --sample is passed or no image_path given, pick a sample from archive
    if not image_path:
        archive_dir = os.path.join(os.path.dirname(__file__), "archive", "animals", "animals")
        if os.path.exists(archive_dir):
            import random
            target_class = args.sample if args.sample else random.choice(os.listdir(archive_dir))
            class_folder = os.path.join(archive_dir, target_class)
            if os.path.isdir(class_folder):
                files = [f for f in os.listdir(class_folder) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
                if files:
                    image_path = os.path.join(class_folder, random.choice(files))
                    print(f"📷 Picked sample image for testing: {image_path}")

    if not image_path:
        print("Please provide an image path or ensure the archive directory exists.")
        sys.exit(1)

    result = predict_image(image_path, model_path=args.model, img_size=args.img_size)

    print("\n" + "=" * 40)
    print("        ANIMAL PREDICTION")
    print("=" * 40)
    print(f"Animal     : {result['predicted_animal'].title()}")
    print(f"Confidence : {result['confidence']:.2f}%")
    print("=" * 40)

    print("\nTOP 5 PREDICTIONS")
    print("-" * 40)
    for item in result["top_5"]:
        bar = "█" * int(item["confidence"] // 5)
        print(f"{item['rank']}. {item['animal'].title():18s} {item['confidence']:6.2f}%  {bar}")
    print("-" * 40)

    print(f"\nStatus     : [{result['tier'].upper()}]")
    print(f"Details    : {result['tier_message']}\n")

    from animal_data import get_animal_info
    info = get_animal_info(result['predicted_animal'])
    print("=" * 50)
    print(f"       ABOUT THE {result['predicted_animal'].upper()}")
    print("=" * 50)
    print(f"🔬 Scientific Name : {info['scientific_name']}")
    print(f"🥩 Diet            : {info['diet']}")
    print(f"🌍 Habitat         : {info['habitat']}")
    print(f"🛡️ Status          : {info['status']}")
    print(f"⏳ Lifespan        : {info['lifespan']}")
    print("\n📖 Overview:")
    print(info['summary'])
    print(f"\n💡 Fun Fact:\n{info['fun_fact']}")
    print("=" * 50 + "\n")


if __name__ == "__main__":
    main()
