"""Day 5: Baseline YOLO training script."""

from ultralytics import YOLO

MODEL = "yolo26n.pt"
DATA_CONFIG = "configs/dataset.yaml"
EPOCHS = 50
IMG_SIZE = 640
BATCH_SIZE = 16
PATIENCE = 20


def main():
    model = YOLO(MODEL)

    results = model.train(
        data=DATA_CONFIG,
        epochs=EPOCHS,
        imgsz=IMG_SIZE,
        batch=BATCH_SIZE,
        patience=PATIENCE,
        project="runs/detect",
        name="baseline",
    )

    print("Training complete.")
    print(f"Best weights saved to: runs/detect/baseline/weights/best.pt")


if __name__ == "__main__":
    main()