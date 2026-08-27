"""Day 2: Dataset audit and image quality checks."""

import os
from pathlib import Path
from PIL import Image

DATASET_ROOT = Path("data/external/cow_dataset/CowAnalysis_Dataset")
SPLITS = ["train", "valid"]
CLASS_NAMES = {0: "Lying", 1: "Standing"}


def check_split(split):
    img_dir = DATASET_ROOT / split / "images"
    lbl_dir = DATASET_ROOT / split / "labels"

    images = sorted([f for f in os.listdir(img_dir) if f.lower().endswith((".jpg", ".jpeg", ".png"))])
    labels = sorted([f for f in os.listdir(lbl_dir) if f.endswith(".txt")])

    image_stems = {Path(f).stem for f in images}
    label_stems = {Path(f).stem for f in labels}

    missing_labels = image_stems - label_stems
    missing_images = label_stems - image_stems

    corrupted = []
    empty_labels = []
    invalid_boxes = []
    class_counts = {0: 0, 1: 0}

    for img_name in images:
        img_path = img_dir / img_name
        try:
            with Image.open(img_path) as im:
                im.verify()
        except Exception:
            corrupted.append(img_name)

    for lbl_name in labels:
        lbl_path = lbl_dir / lbl_name
        with open(lbl_path) as f:
            lines = [l.strip() for l in f.readlines() if l.strip()]
        if not lines:
            empty_labels.append(lbl_name)
            continue
        for line in lines:
            parts = line.split()
            cls = int(parts[0])
            xc, yc, bw, bh = map(float, parts[1:5])
            if not (0 <= xc <= 1 and 0 <= yc <= 1 and 0 < bw <= 1 and 0 < bh <= 1):
                invalid_boxes.append((lbl_name, line))
            if cls in class_counts:
                class_counts[cls] += 1

    return {
        "split": split,
        "num_images": len(images),
        "num_labels": len(labels),
        "missing_labels": missing_labels,
        "missing_images": missing_images,
        "corrupted": corrupted,
        "empty_labels": empty_labels,
        "invalid_boxes": invalid_boxes,
        "class_counts": class_counts,
    }


def print_report(result):
    print(f"\n{'='*50}")
    print(f"SPLIT: {result['split']}")
    print(f"{'='*50}")
    print(f"Images: {result['num_images']}  |  Labels: {result['num_labels']}")

    if result["missing_labels"]:
        print(f"⚠️  {len(result['missing_labels'])} images missing label files")
    else:
        print("✅ All images have matching labels")

    if result["missing_images"]:
        print(f"⚠️  {len(result['missing_images'])} labels missing image files")

    if result["corrupted"]:
        print(f"⚠️  {len(result['corrupted'])} corrupted images: {result['corrupted'][:5]}")
    else:
        print("✅ No corrupted images found")

    if result["empty_labels"]:
        print(f"⚠️  {len(result['empty_labels'])} empty label files")
    else:
        print("✅ No empty label files")

    if result["invalid_boxes"]:
        print(f"⚠️  {len(result['invalid_boxes'])} invalid bounding boxes")
    else:
        print("✅ All bounding boxes are valid")

    total = sum(result["class_counts"].values())
    print(f"\nClass balance ({total} total boxes):")
    for cls_id, count in result["class_counts"].items():
        pct = (count / total * 100) if total else 0
        print(f"  {CLASS_NAMES[cls_id]} (class {cls_id}): {count} ({pct:.1f}%)")


if __name__ == "__main__":
    all_results = []
    for split in SPLITS:
        result = check_split(split)
        all_results.append(result)
        print_report(result)

    print(f"\n{'='*50}")
    print("AUDIT COMPLETE")
    print(f"{'='*50}")
    