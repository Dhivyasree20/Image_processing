"""Day 7: Model evaluation and comparison."""

from ultralytics import YOLO

MODEL_PATH = "/content/drive/MyDrive/Image_processing_backup/runs/detect/improved_s/weights/best.pt"
DATA_CONFIG = "configs/dataset.yaml"


def main():
    model = YOLO(MODEL_PATH)

    print("Evaluating on TEST split (held-out, never used in training or tuning)...")
    results = model.val(data=DATA_CONFIG, split="test")

    print("\n" + "=" * 50)
    print("FINAL TEST SET RESULTS")
    print("=" * 50)
    print(f"mAP50: {results.box.map50:.3f}")
    print(f"mAP50-95: {results.box.map:.3f}")
    print(f"Precision: {results.box.mp:.3f}")
    print(f"Recall: {results.box.mr:.3f}")


if __name__ == "__main__":
    main()