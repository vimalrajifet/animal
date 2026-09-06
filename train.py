"""
90-Class Animal Classification Training Script
Architecture: EfficientNetB3 + Custom Head with 2-Stage Transfer Learning & Fine-Tuning
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

import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras import layers, Model
from tensorflow.keras.applications import EfficientNetB3
from tensorflow.keras.layers import GlobalAveragePooling2D, Dense, Dropout


def check_gpu():
    print("=" * 50)
    print("ENVIRONMENT CHECK")
    print("=" * 50)
    print("TensorFlow version:", tf.__version__)
    gpu = tf.config.list_physical_devices("GPU")
    if gpu:
        print("✅ GPU detected:", gpu)
    else:
        print("⚠️ No GPU detected. Running on CPU.")
        print("Tip: If you want faster training, you can also run this on Google Colab with T4 GPU.")
    print("=" * 50)


def find_animal_directory(default_path=None):
    if default_path and os.path.exists(default_path):
        return default_path

    # Check known local path candidates
    candidates = [
        os.path.join(os.path.dirname(__file__), "archive", "animals", "animals"),
        os.path.join(os.path.dirname(__file__), "archive", "animals"),
        r"c:\Users\vimal\Downloads\animals\archive\animals\animals",
        r"c:\Users\vimal\Downloads\animals\archive\animals",
    ]

    for cand in candidates:
        if os.path.exists(cand):
            subdirs = [d for d in os.listdir(cand) if os.path.isdir(os.path.join(cand, d)) and not d.startswith(".")]
            if len(subdirs) >= 80:
                return cand

    # Walk from script directory
    for root, dirs, files in os.walk(os.path.dirname(__file__)):
        subdirs = [d for d in dirs if not d.startswith(".")]
        if len(subdirs) >= 80:
            return root

    raise ValueError("Could not automatically locate the 90 animal class folders. Please pass --data_dir.")


def build_augmentation():
    return tf.keras.Sequential([
        layers.RandomFlip("horizontal"),
        layers.RandomRotation(0.08),
        layers.RandomZoom(0.10),
        layers.RandomTranslation(height_factor=0.05, width_factor=0.05),
        layers.RandomContrast(0.10)
    ], name="data_augmentation")


def build_model(num_classes, img_size):
    # Pretrained EfficientNetB3 backbone
    base_model = EfficientNetB3(
        weights="imagenet",
        include_top=False,
        input_shape=(img_size, img_size, 3)
    )
    base_model.trainable = False

    data_augmentation = build_augmentation()

    inputs = tf.keras.Input(shape=(img_size, img_size, 3))
    x = data_augmentation(inputs)
    x = base_model(x, training=False)
    x = GlobalAveragePooling2D()(x)
    x = Dropout(0.35)(x)
    outputs = Dense(num_classes, activation="softmax")(x)

    model = Model(inputs, outputs, name="Animal_EfficientNetB3")
    return model, base_model


def plot_and_save_history(history, history_fine, output_path="training_performance.png"):
    train_acc = history.history["accuracy"]
    val_acc = history.history["val_accuracy"]
    train_loss = history.history["loss"]
    val_loss = history.history["val_loss"]

    if history_fine:
        train_acc += history_fine.history["accuracy"]
        val_acc += history_fine.history["val_accuracy"]
        train_loss += history_fine.history["loss"]
        val_loss += history_fine.history["val_loss"]

    epochs_range = range(1, len(train_acc) + 1)

    plt.figure(figsize=(14, 5))

    plt.subplot(1, 2, 1)
    plt.plot(epochs_range, train_acc, label="Training Accuracy", color="#2563eb", linewidth=2)
    plt.plot(epochs_range, val_acc, label="Validation Accuracy", color="#16a34a", linewidth=2)
    plt.xlabel("Epoch")
    plt.ylabel("Accuracy")
    plt.title("EfficientNetB3 Animal Classification Accuracy")
    plt.legend(loc="lower right")
    plt.grid(True, linestyle="--", alpha=0.6)

    plt.subplot(1, 2, 2)
    plt.plot(epochs_range, train_loss, label="Training Loss", color="#dc2626", linewidth=2)
    plt.plot(epochs_range, val_loss, label="Validation Loss", color="#ea580c", linewidth=2)
    plt.xlabel("Epoch")
    plt.ylabel("Loss")
    plt.title("EfficientNetB3 Animal Classification Loss")
    plt.legend(loc="upper right")
    plt.grid(True, linestyle="--", alpha=0.6)

    plt.tight_layout()
    plt.savefig(output_path, dpi=200)
    print(f"📊 Training curves saved to {output_path}")


def main():
    parser = argparse.ArgumentParser(description="Train 90-Class Animal Classification Model")
    parser.add_argument("--data_dir", type=str, default=None, help="Path to animal class directories")
    parser.add_argument("--img_size", type=int, default=300, help="Image size (default 300 for EfficientNetB3)")
    parser.add_argument("--batch_size", type=int, default=16, help="Batch size")
    parser.add_argument("--seed", type=int, default=123, help="Random seed")
    parser.add_argument("--initial_epochs", type=int, default=15, help="Initial epochs with frozen backbone")
    parser.add_argument("--fine_tune_epochs", type=int, default=20, help="Fine-tuning epochs")
    parser.add_argument("--output_model", type=str, default="best_animal_model.keras", help="Model save filename")
    parser.add_argument("--quick", action="store_true", help="Quick run mode for testing the pipeline")
    args = parser.parse_args()

    check_gpu()

    data_dir = find_animal_directory(args.data_dir)
    print("\n✅ Animal dataset folder:", data_dir)

    classes = sorted([
        name for name in os.listdir(data_dir)
        if os.path.isdir(os.path.join(data_dir, name)) and not name.startswith(".")
    ])
    num_classes = len(classes)
    print(f"✅ Discovered {num_classes} animal classes.")

    # Save classes.json
    classes_path = os.path.join(os.path.dirname(__file__), "classes.json")
    with open(classes_path, "w", encoding="utf-8") as f:
        json.dump(classes, f, indent=2)
    print(f"Saved class list to {classes_path}")

    # Datasets
    print("\nLoading datasets...")
    train_ds = tf.keras.utils.image_dataset_from_directory(
        data_dir,
        validation_split=0.20,
        subset="training",
        seed=args.seed,
        image_size=(args.img_size, args.img_size),
        batch_size=args.batch_size,
        label_mode="int"
    )

    val_ds = tf.keras.utils.image_dataset_from_directory(
        data_dir,
        validation_split=0.20,
        subset="validation",
        seed=args.seed,
        image_size=(args.img_size, args.img_size),
        batch_size=args.batch_size,
        label_mode="int"
    )

    autotune = tf.data.AUTOTUNE
    train_ds = train_ds.prefetch(buffer_size=autotune)
    val_ds = val_ds.prefetch(buffer_size=autotune)
    print("✅ Dataset optimization completed.")

    if args.quick:
        print("\n⚡ QUICK MODE ENABLED (fast verification on CPU)")
        initial_epochs = 1
        fine_tune_epochs = 1
        train_ds = train_ds.take(25)
        val_ds = val_ds.take(10)
    else:
        initial_epochs = args.initial_epochs
        fine_tune_epochs = args.fine_tune_epochs

    # Build model
    print("\nBuilding EfficientNetB3 architecture...")
    model, base_model = build_model(num_classes, args.img_size)
    model.summary()

    # Compile Stage 1
    model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
        loss=tf.keras.losses.SparseCategoricalCrossentropy(),
        metrics=["accuracy"]
    )
    print("✅ Model compiled for Stage 1.")

    callbacks = [
        tf.keras.callbacks.ModelCheckpoint(
            args.output_model,
            monitor="val_accuracy",
            save_best_only=True,
            mode="max",
            verbose=1
        ),
        tf.keras.callbacks.EarlyStopping(
            monitor="val_loss",
            patience=5,
            restore_best_weights=True,
            verbose=1
        ),
        tf.keras.callbacks.ReduceLROnPlateau(
            monitor="val_loss",
            factor=0.3,
            patience=2,
            min_lr=1e-7,
            verbose=1
        )
    ]

    print(f"\n🚀 Phase 1: Training top layers ({initial_epochs} epochs)...")
    history = model.fit(
        train_ds,
        validation_data=val_ds,
        epochs=initial_epochs,
        callbacks=callbacks
    )

    print("\n🚀 Phase 2: Unfreezing top 60 layers for fine-tuning...")
    base_model.trainable = True
    for layer in base_model.layers[:-60]:
        layer.trainable = False
    for layer in base_model.layers:
        if isinstance(layer, tf.keras.layers.BatchNormalization):
            layer.trainable = False

    model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=1e-5),
        loss=tf.keras.losses.SparseCategoricalCrossentropy(),
        metrics=["accuracy"]
    )
    print("✅ Fine-tuning compiled with lr=1e-5.")

    history_fine = model.fit(
        train_ds,
        validation_data=val_ds,
        epochs=fine_tune_epochs,
        callbacks=callbacks
    )

    # Save model if not already saved
    if not os.path.exists(args.output_model):
        model.save(args.output_model)

    print(f"\n✅ Loading best model from {args.output_model} for final evaluation...")
    best_model = tf.keras.models.load_model(args.output_model)
    val_loss, val_accuracy = best_model.evaluate(val_ds)

    print("\n==============================")
    print("FINAL MODEL PERFORMANCE")
    print("==============================")
    print(f"Validation Accuracy : {val_accuracy * 100:.2f}%")
    print(f"Validation Loss     : {val_loss:.4f}")
    print("==============================")

    plot_and_save_history(history, history_fine)
    print(f"\n🎉 Training completed successfully! Model saved at: {args.output_model}")


if __name__ == "__main__":
    main()
