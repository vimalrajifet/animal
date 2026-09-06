"""
Generate animal_classification.ipynb notebook matching the user's 21-cell workflow.
"""
import json
import os

cells = [
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "# 🐾 90-Class Animal Classification with EfficientNetB3\n",
            "\n",
            "This notebook builds a high-accuracy, 90-class animal image classifier using **EfficientNetB3** and two-stage transfer learning with TensorFlow/Keras.\n",
            "\n",
            "### Pipeline Architecture:\n",
            "1. **Image Validation & Preprocessing** (300x300 RGB)\n",
            "2. **Data Augmentation** (Flips, Rotations, Zooms, Translations, Contrast)\n",
            "3. **Pretrained EfficientNetB3 Backbone** (ImageNet weights)\n",
            "4. **Stage 1**: Train custom classification head with frozen backbone\n",
            "5. **Stage 2**: Fine-tune top 60 layers with low learning rate (1e-5)\n",
            "6. **Top-5 Animal Predictions & Confidence Tiers**"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": ["## Cell 1 — Check GPU"]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "import tensorflow as tf\n",
            "\n",
            "print(\"TensorFlow version:\", tf.__version__)\n",
            "\n",
            "gpu = tf.config.list_physical_devices(\"GPU\")\n",
            "\n",
            "if gpu:\n",
            "    print(\"✅ GPU detected:\", gpu)\n",
            "else:\n",
            "    print(\"⚠️ No GPU detected.\")\n",
            "    print(\"Go to Runtime > Change runtime type > T4 GPU (if on Google Colab)\")\n"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": ["## Cell 2 — Download or locate the animal dataset"]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "import os\n",
            "\n",
            "# Check if dataset exists locally first\n",
            "local_path = os.path.join(\"archive\", \"animals\", \"animals\")\n",
            "if os.path.exists(local_path):\n",
            "    dataset_path = os.path.abspath(local_path)\n",
            "    print(\"✅ Found existing local dataset at:\", dataset_path)\n",
            "else:\n",
            "    try:\n",
            "        import kagglehub\n",
            "        dataset_path = kagglehub.dataset_download(\n",
            "            \"iamsouravbanerjee/animal-image-dataset-90-different-animals\"\n",
            "        )\n",
            "        print(\"✅ Dataset downloaded from KaggleHub\")\n",
            "    except Exception as e:\n",
            "        dataset_path = \".\"\n",
            "        print(\"⚠️ KaggleHub download skipped or error:\", e)\n",
            "\n",
            "print(\"Dataset path:\", dataset_path)\n"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "## Cell 3 — Automatically find the 90 animal folders\n",
            "\n",
            "This avoids path problems across both Colab and local environments."
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "import os\n",
            "\n",
            "def find_animal_directory(root_path):\n",
            "    candidates = []\n",
            "    for root, dirs, files in os.walk(root_path):\n",
            "        # Count subfolders\n",
            "        subdirs = [d for d in dirs if not d.startswith(\".\")]\n",
            "        # We expect around 90 animal folders\n",
            "        if len(subdirs) >= 80:\n",
            "            candidates.append(root)\n",
            "\n",
            "    if not candidates:\n",
            "        raise ValueError(\"Could not find animal class folders.\")\n",
            "\n",
            "    return candidates[0]\n",
            "\n",
            "DATA_DIR = find_animal_directory(dataset_path)\n",
            "\n",
            "print(\"✅ Animal dataset folder:\")\n",
            "print(DATA_DIR)\n",
            "\n",
            "classes = sorted([\n",
            "    name for name in os.listdir(DATA_DIR)\n",
            "    if os.path.isdir(os.path.join(DATA_DIR, name))\n",
            "])\n",
            "\n",
            "print(\"\\nNumber of animal classes:\", len(classes))\n",
            "print(\"\\nAnimals:\")\n",
            "print(classes)\n"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "## Cell 4 — Settings\n",
            "\n",
            "EfficientNetB3 normally uses a 300 × 300 image size."
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "IMG_SIZE = 300\n",
            "BATCH_SIZE = 16\n",
            "SEED = 123\n",
            "VALIDATION_SPLIT = 0.20\n"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": ["## Cell 5 — Create training and validation datasets"]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "import tensorflow as tf\n",
            "\n",
            "train_ds = tf.keras.utils.image_dataset_from_directory(\n",
            "    DATA_DIR,\n",
            "    validation_split=VALIDATION_SPLIT,\n",
            "    subset=\"training\",\n",
            "    seed=SEED,\n",
            "    image_size=(IMG_SIZE, IMG_SIZE),\n",
            "    batch_size=BATCH_SIZE,\n",
            "    label_mode=\"int\"\n",
            ")\n",
            "\n",
            "val_ds = tf.keras.utils.image_dataset_from_directory(\n",
            "    DATA_DIR,\n",
            "    validation_split=VALIDATION_SPLIT,\n",
            "    subset=\"validation\",\n",
            "    seed=SEED,\n",
            "    image_size=(IMG_SIZE, IMG_SIZE),\n",
            "    batch_size=BATCH_SIZE,\n",
            "    label_mode=\"int\"\n",
            ")\n",
            "\n",
            "class_names = train_ds.class_names\n",
            "NUM_CLASSES = len(class_names)\n",
            "\n",
            "print(\"\\n✅ Number of classes:\", NUM_CLASSES)\n",
            "print(class_names)\n"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": ["## Cell 6 — Improve data-loading speed"]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "AUTOTUNE = tf.data.AUTOTUNE\n",
            "\n",
            "train_ds = train_ds.prefetch(buffer_size=AUTOTUNE)\n",
            "val_ds = val_ds.prefetch(buffer_size=AUTOTUNE)\n",
            "\n",
            "print(\"✅ Dataset optimization completed\")\n"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "## Cell 7 — Data augmentation\n",
            "\n",
            "This helps reduce overfitting."
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "from tensorflow.keras import layers\n",
            "\n",
            "data_augmentation = tf.keras.Sequential([\n",
            "    layers.RandomFlip(\"horizontal\"),\n",
            "    layers.RandomRotation(0.08),\n",
            "    layers.RandomZoom(0.10),\n",
            "    layers.RandomTranslation(height_factor=0.05, width_factor=0.05),\n",
            "    layers.RandomContrast(0.10)\n",
            "], name=\"data_augmentation\")\n"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": ["## Cell 8 — Create EfficientNetB3 deep-learning model"]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "from tensorflow.keras.applications import EfficientNetB3\n",
            "from tensorflow.keras import Model\n",
            "from tensorflow.keras.layers import GlobalAveragePooling2D, Dense, Dropout\n",
            "\n",
            "# Load pretrained EfficientNetB3\n",
            "base_model = EfficientNetB3(\n",
            "    weights=\"imagenet\",\n",
            "    include_top=False,\n",
            "    input_shape=(IMG_SIZE, IMG_SIZE, 3)\n",
            ")\n",
            "\n",
            "# Freeze pretrained network first\n",
            "base_model.trainable = False\n",
            "\n",
            "# Input\n",
            "inputs = tf.keras.Input(shape=(IMG_SIZE, IMG_SIZE, 3))\n",
            "\n",
            "# Data augmentation\n",
            "x = data_augmentation(inputs)\n",
            "\n",
            "# EfficientNet feature extraction\n",
            "x = base_model(x, training=False)\n",
            "\n",
            "# Global pooling\n",
            "x = GlobalAveragePooling2D()(x)\n",
            "\n",
            "# Dropout\n",
            "x = Dropout(0.35)(x)\n",
            "\n",
            "# Classification layer\n",
            "outputs = Dense(NUM_CLASSES, activation=\"softmax\")(x)\n",
            "\n",
            "model = Model(inputs, outputs)\n",
            "model.summary()\n"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": ["## Cell 9 — Compile model"]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "model.compile(\n",
            "    optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),\n",
            "    loss=tf.keras.losses.SparseCategoricalCrossentropy(),\n",
            "    metrics=[\"accuracy\"]\n",
            ")\n",
            "\n",
            "print(\"✅ Model compiled\")\n"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "## Cell 10 — Callbacks\n",
            "\n",
            "These help the model automatically keep its best version."
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "callbacks = [\n",
            "    tf.keras.callbacks.ModelCheckpoint(\n",
            "        \"best_animal_model.keras\",\n",
            "        monitor=\"val_accuracy\",\n",
            "        save_best_only=True,\n",
            "        mode=\"max\",\n",
            "        verbose=1\n",
            "    ),\n",
            "    tf.keras.callbacks.EarlyStopping(\n",
            "        monitor=\"val_loss\",\n",
            "        patience=5,\n",
            "        restore_best_weights=True,\n",
            "        verbose=1\n",
            "    ),\n",
            "    tf.keras.callbacks.ReduceLROnPlateau(\n",
            "        monitor=\"val_loss\",\n",
            "        factor=0.3,\n",
            "        patience=2,\n",
            "        min_lr=1e-7,\n",
            "        verbose=1\n",
            "    )\n",
            "]\n"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "## Cell 11 — First training\n",
            "\n",
            "At this stage the pretrained EfficientNet weights are frozen. Only your new animal-classification layer is learning."
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "INITIAL_EPOCHS = 15\n",
            "\n",
            "history = model.fit(\n",
            "    train_ds,\n",
            "    validation_data=val_ds,\n",
            "    epochs=INITIAL_EPOCHS,\n",
            "    callbacks=callbacks\n",
            ")\n"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "## Cell 12 — Fine-tune EfficientNetB3\n",
            "\n",
            "Fine-tuning is one of the most important steps for better accuracy."
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "# Unfreeze the model\n",
            "base_model.trainable = True\n",
            "\n",
            "print(\"Total EfficientNet layers:\", len(base_model.layers))\n",
            "\n",
            "# Keep most layers frozen\n",
            "# Fine-tune only the last 60 layers\n",
            "for layer in base_model.layers[:-60]:\n",
            "    layer.trainable = False\n",
            "\n",
            "# Keep BatchNormalization layers frozen\n",
            "for layer in base_model.layers:\n",
            "    if isinstance(layer, tf.keras.layers.BatchNormalization):\n",
            "        layer.trainable = False\n",
            "\n",
            "print(\"✅ Fine tuning enabled\")\n"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "## Cell 13 — Compile using a very small learning rate\n",
            "\n",
            "This is important. Don't use 0.001 during fine-tuning."
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "model.compile(\n",
            "    optimizer=tf.keras.optimizers.Adam(learning_rate=1e-5),\n",
            "    loss=tf.keras.losses.SparseCategoricalCrossentropy(),\n",
            "    metrics=[\"accuracy\"]\n",
            ")\n"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": ["## Cell 14 — Fine-tune"]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "FINE_TUNE_EPOCHS = 20\n",
            "\n",
            "history_fine = model.fit(\n",
            "    train_ds,\n",
            "    validation_data=val_ds,\n",
            "    epochs=FINE_TUNE_EPOCHS,\n",
            "    callbacks=callbacks\n",
            ")\n"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": ["## Cell 15 — Load the best model"]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "model = tf.keras.models.load_model(\"best_animal_model.keras\")\n",
            "print(\"✅ Best model loaded\")\n"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": ["## Cell 16 — Check validation accuracy"]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "val_loss, val_accuracy = model.evaluate(val_ds)\n",
            "\n",
            "print(\"\\n==============================\")\n",
            "print(\"MODEL PERFORMANCE\")\n",
            "print(\"==============================\")\n",
            "print(f\"Validation Accuracy : {val_accuracy * 100:.2f}%\")\n",
            "print(f\"Validation Loss     : {val_loss:.4f}\")\n"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": ["## Cell 17 — Plot accuracy graph"]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "import matplotlib.pyplot as plt\n",
            "\n",
            "train_accuracy = history.history[\"accuracy\"] + history_fine.history[\"accuracy\"]\n",
            "validation_accuracy = history.history[\"val_accuracy\"] + history_fine.history[\"val_accuracy\"]\n",
            "\n",
            "plt.figure(figsize=(10, 6))\n",
            "plt.plot(train_accuracy, label=\"Training Accuracy\")\n",
            "plt.plot(validation_accuracy, label=\"Validation Accuracy\")\n",
            "plt.xlabel(\"Epoch\")\n",
            "plt.ylabel(\"Accuracy\")\n",
            "plt.title(\"EfficientNetB3 Animal Classification Accuracy\")\n",
            "plt.legend()\n",
            "plt.grid()\n",
            "plt.show()\n"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": ["## Cell 18 — Upload or select animal image"]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "import os\n",
            "try:\n",
            "    from google.colab import files\n",
            "    uploaded = files.upload()\n",
            "    filename = list(uploaded.keys())[0]\n",
            "except Exception:\n",
            "    # Local fallback: select sample image from archive or local path\n",
            "    sample_dir = os.path.join(DATA_DIR, \"tiger\")\n",
            "    sample_images = [f for f in os.listdir(sample_dir) if f.lower().endswith(('.jpg', '.png'))]\n",
            "    filename = os.path.join(sample_dir, sample_images[0])\n",
            "    print(\"Using local test image:\", filename)\n"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": ["## Cell 19 — Predict the uploaded animal"]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "import numpy as np\n",
            "import matplotlib.pyplot as plt\n",
            "from PIL import Image\n",
            "\n",
            "# Load image\n",
            "img = Image.open(filename).convert(\"RGB\")\n",
            "\n",
            "# Show uploaded image\n",
            "plt.figure(figsize=(6, 6))\n",
            "plt.imshow(img)\n",
            "plt.axis(\"off\")\n",
            "plt.title(\"Uploaded Animal\")\n",
            "plt.show()\n",
            "\n",
            "# Resize image\n",
            "img_resized = img.resize((IMG_SIZE, IMG_SIZE))\n",
            "\n",
            "# Convert to numpy\n",
            "img_array = np.array(img_resized, dtype=np.float32)\n",
            "\n",
            "# Add batch dimension\n",
            "img_array = np.expand_dims(img_array, axis=0)\n",
            "\n",
            "# Prediction\n",
            "prediction = model.predict(img_array, verbose=0)[0]\n",
            "\n",
            "# Best prediction\n",
            "predicted_index = np.argmax(prediction)\n",
            "predicted_animal = class_names[predicted_index]\n",
            "confidence = prediction[predicted_index] * 100\n",
            "\n",
            "print(\"\\n================================\")\n",
            "print(\"        ANIMAL PREDICTION\")\n",
            "print(\"================================\")\n",
            "print(f\"Animal     : {predicted_animal.title()}\")\n",
            "print(f\"Confidence : {confidence:.2f}%\")\n",
            "print(\"================================\")\n"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": ["## Cell 20 — Show Top 5 predictions"]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "top_5_indices = np.argsort(prediction)[-5:][::-1]\n",
            "\n",
            "print(\"\\nTOP 5 PREDICTIONS\")\n",
            "print(\"-\" * 35)\n",
            "\n",
            "for rank, index in enumerate(top_5_indices, start=1):\n",
            "    animal = class_names[index]\n",
            "    score = prediction[index] * 100\n",
            "    print(f\"{rank}. {animal.title():20s} {score:.2f}%\")\n"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": ["## Cell 21 — Better confidence handling"]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "if confidence >= 80:\n",
            "    print(f\"✅ High confidence: This animal is most likely a {predicted_animal.title()}.\")\n",
            "elif confidence >= 50:\n",
            "    print(f\"⚠️ Medium confidence: The animal may be a {predicted_animal.title()}.\")\n",
            "else:\n",
            "    print(\"❓ Low confidence prediction.\")\n",
            "    print(f\"Best guess: {predicted_animal.title()}\")\n"
        ]
    }
]

notebook = {
    "cells": cells,
    "metadata": {
        "language_info": {
            "name": "python",
            "version": "3.11"
        },
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3"
        }
    },
    "nbformat": 4,
    "nbformat_minor": 2
}

output_path = r"c:\Users\vimal\Downloads\animals\animal_classification.ipynb"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(notebook, f, indent=2)

print("Notebook generated at:", output_path)
