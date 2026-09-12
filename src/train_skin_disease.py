"""Day 8 (revised scope): Train skin disease classifier/detector."""

from ultralytics import YOLO

MODEL = "yolo26s.pt"
DATA_CONFIG = "configs/skin_disease_dataset.yaml"
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
        name="skin_disease_v1",
    )

    print("Training complete.")
    print(f"Best weights saved to: runs/detect/skin_disease_v1/weights/best.pt")


if __name__ == "__main__":
    main()