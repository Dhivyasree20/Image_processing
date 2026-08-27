"""Day 3: Visual spot-check of a random sample of labeled images."""

import os
import random
import cv2
import matplotlib.pyplot as plt
from pathlib import Path

DATASET_ROOT = Path("data/external/cow_dataset/CowAnalysis_Dataset")
SPLIT = "train"
SAMPLE_SIZE = 16
SEED = 42

CLASS_NAMES = {0: "Lying", 1: "Standing"}
CLASS_COLORS = {0: (0, 255, 0), 1: (0, 0, 255)}  # green=Lying, red=Standing


def draw_boxes(img_path, lbl_path):
    img = cv2.imread(str(img_path))
    h, w = img.shape[:2]
    with open(lbl_path) as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]
    for line in lines:
        parts = line.split()
        cls = int(parts[0])
        xc, yc, bw, bh = map(float, parts[1:5])
        x1 = int((xc - bw / 2) * w)
        y1 = int((yc - bh / 2) * h)
        x2 = int((xc + bw / 2) * w)
        y2 = int((yc + bh / 2) * h)
        color = CLASS_COLORS.get(cls, (255, 255, 0))
        cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


def main():
    img_dir = DATASET_ROOT / SPLIT / "images"
    lbl_dir = DATASET_ROOT / SPLIT / "labels"

    images = sorted([f for f in os.listdir(img_dir) if f.lower().endswith((".jpg", ".jpeg", ".png"))])

    random.seed(SEED)
    sample = random.sample(images, min(SAMPLE_SIZE, len(images)))

    cols = 4
    rows = (len(sample) + cols - 1) // cols
    fig, axes = plt.subplots(rows, cols, figsize=(20, 5 * rows))
    axes = axes.flatten()

    for i, img_name in enumerate(sample):
        lbl_name = img_name.rsplit(".", 1)[0] + ".txt"
        img_path = img_dir / img_name
        lbl_path = lbl_dir / lbl_name

        vis = draw_boxes(img_path, lbl_path)
        axes[i].imshow(vis)
        axes[i].set_title(img_name, fontsize=7)
        axes[i].axis("off")

    for j in range(len(sample), len(axes)):
        axes[j].axis("off")

    plt.tight_layout()
    plt.savefig("reports/figures/day3_visual_spotcheck.png", dpi=150, bbox_inches="tight")
    print(f"Saved grid of {len(sample)} images to reports/figures/day3_visual_spotcheck.png")
    print("Legend: GREEN = Lying (class 0), RED = Standing (class 1)")


if __name__ == "__main__":
    main()
    