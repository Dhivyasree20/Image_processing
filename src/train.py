"""Day 5: Baseline YOLO training script."""

from ultralytics import YOLO

MODEL = "yolo26s.pt"
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
        project="/content/drive/MyDrive/Image_processing_backup/runs/detect",
        name="improved_s",
    )

    print("Training complete.")
    print(f"Best weights saved to: runs/detect/baseline/weights/best.pt")


if __name__ == "__main__":
    main()
    