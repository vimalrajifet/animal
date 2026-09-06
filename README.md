# 🐾 90-Class Animal Classification with EfficientNetB3

A complete end-to-end Deep Learning vision pipeline trained on the 90-class animal dataset located in `archive/animals/animals`.

---

## 🚀 Quick Start Guide

### 1. Launch the Interactive Web Application with Voice Narration
Run the Streamlit application to upload your own animal images, hear live speech narration, or test sample images directly from the 90-class archive gallery:

```bash
streamlit run app.py
```

Features:
- **🗣️ Live Voice Narration (Say About This Animal)**: Speaks out loud facts about the predicted animal using the browser Web Speech API.
- **Auto-Speak Mode**: Toggleable option to automatically speak facts as soon as an image is classified.
- **Image Uploader**: Drag & drop any JPG, PNG, or WEBP animal image.
- **Archive Gallery Picker**: Select any of the 90 animal classes and test real sample photos instantly with a single click.
- **Top Prediction Card**: Best guess animal name with emoji, confidence percentage, and tier badge.
- **Top 5 Probability Bars**: Visual breakdown of the top 5 predicted animal species.
- **📖 Wildlife Encyclopedia**: Scientific name, diet, natural habitat, conservation status, lifespan, and fascinating fun facts.

---

### 2. Standalone Modern Web App (FastAPI + HTML5)
You can also launch a dedicated modern website with full drag-and-drop and voice synthesis:

```bash
python server.py
```
Open **http://127.0.0.1:8000** in your browser.

---

### 2. Predict Animals from the Command Line
Run CLI inference on any image:

```bash
# Test a specific image file
python predict.py path/to/image.jpg

# Or pick a random sample from the dataset (e.g. tiger, elephant, panda)
python predict.py --sample tiger
python predict.py --sample panda
```

Example output:
```text
========================================
        ANIMAL PREDICTION
========================================
Animal     : Tiger
Confidence : 96.84%
========================================

TOP 5 PREDICTIONS
----------------------------------------
1. Tiger                96.84%  ███████████████████
2. Leopard               1.71%  
3. Lion                  0.82%  
4. Cheetah               0.31%  
5. Hyena                 0.09%  
----------------------------------------

Status     : [HIGH CONFIDENCE]
Details    : High confidence: This animal is most likely a Tiger.
```

---

### 3. Model Training
The dataset contains 5,400 images across 90 animal classes.

#### Quick Verification Run (Fast check on CPU):
```bash
python train.py --quick
```

#### Full Production Training:
```bash
python train.py --initial_epochs 15 --fine_tune_epochs 20 --batch_size 16 --img_size 300
```
Key Training Features:
- **Data Augmentation**: `RandomFlip`, `RandomRotation`, `RandomZoom`, `RandomTranslation`, `RandomContrast`.
- **Pretrained Backbone**: EfficientNetB3 initialized with ImageNet weights.
- **Stage 1 (Transfer Learning)**: Frozen base model, learning custom dense classification layers.
- **Stage 2 (Fine-Tuning)**: Unfreezes the top 60 layers with low learning rate (`1e-5`) for maximum accuracy.
- **Callbacks**: `ModelCheckpoint` saving to `best_animal_model.keras`, `EarlyStopping`, and `ReduceLROnPlateau`.
- **Metrics Plot**: Automatically saves `training_performance.png`.

---

### 4. Jupyter Notebook
Open [`animal_classification.ipynb`](file:///c:/Users/vimal/Downloads/animals/animal_classification.ipynb) in VS Code, JupyterLab, or upload it to **Google Colab** to train on a GPU runtime (T4 GPU). It contains all 21 modular cells matching your pipeline.

---

## 📁 Project Structure

```text
animals/
├── app.py                      # Interactive Streamlit Web Application
├── predict.py                  # Standalone CLI prediction tool
├── train.py                    # Complete 2-stage transfer learning training script
├── animal_classification.ipynb # Full 21-cell Jupyter / Colab notebook
├── best_animal_model.keras     # Trained EfficientNetB3 model weights
├── classes.json                # Canonical list of all 90 animal classes
├── training_performance.png    # Validation and training accuracy/loss curves
├── README.md                   # Project guide and instructions
└── archive/
    ├── name of the animals.txt # List of 90 animals
    └── animals/
        └── animals/            # 90 class folders (antelope, ..., zebra)
```
