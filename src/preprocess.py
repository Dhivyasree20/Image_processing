"""Day 4: Preprocessing, train/val/test splitting."""

import random
import shutil
from pathlib import Path

DATASET_ROOT = Path("data/external/cow_dataset/CowAnalysis_Dataset")
TEST_FRACTION = 0.12
SEED = 42


def main():
    train_img_dir = DATASET_ROOT / "train" / "images"
    train_lbl_dir = DATASET_ROOT / "train" / "labels"

    test_img_dir = DATASET_ROOT / "test" / "images"
    test_lbl_dir = DATASET_ROOT / "test" / "labels"
    test_img_dir.mkdir(parents=True, exist_ok=True)
    test_lbl_dir.mkdir(parents=True, exist_ok=True)

    images = sorted([f.name for f in train_img_dir.iterdir() if f.suffix.lower() in (".jpg", ".jpeg", ".png")])

    random.seed(SEED)
    n_test = int(len(images) * TEST_FRACTION)
    test_images = set(random.sample(images, n_test))

    for img_name in test_images:
        lbl_name = Path(img_name).stem + ".txt"
        shutil.move(str(train_img_dir / img_name), str(test_img_dir / img_name))
        shutil.move(str(train_lbl_dir / lbl_name), str(test_lbl_dir / lbl_name))

    remaining_train = len(list(train_img_dir.iterdir()))
    n_valid = len(list((DATASET_ROOT / "valid" / "images").iterdir()))
    n_test_final = len(list(test_img_dir.iterdir()))

    total = remaining_train + n_valid + n_test_final
    print(f"Split complete:")
    print(f"  Train: {remaining_train} ({remaining_train/total*100:.1f}%)")
    print(f"  Valid: {n_valid} ({n_valid/total*100:.1f}%)")
    print(f"  Test:  {n_test_final} ({n_test_final/total*100:.1f}%)")


if __name__ == "__main__":
    main()