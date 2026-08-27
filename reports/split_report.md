# Day 4 Deliverable: Train/Val/Test Split

**Project:** Cow Image Processing & Health Assessment using YOLO
**Date:** Day 4

## Context

The Zenodo dataset (via Roboflow export) shipped with only `train` and `valid` splits — no
held-out `test` set. A proper evaluation workflow requires a third split that the model never
sees during training or hyperparameter tuning, used exactly once at the end (Day 7) for an
honest, unbiased performance report.

## Method

Ran `src/preprocess.py`, which randomly samples 12% of the `train` split (seed=42, for
reproducibility) and moves the corresponding image + label pairs into a new `test` split.
`valid` was left untouched since it already serves its intended tuning purpose.

## Result

| Split | Images | % of total |
|-------|--------|------------|
| Train | 542    | 70.6%      |
| Valid | 153    | 19.9%      |
| Test  | 73     | 9.5%       |
| **Total** | **768** | **100%** |

(Total is 768, not 769, reflecting the 1 image excluded on Day 2 for the unlabeled
annotation gap.)

Split ratio approximates the standard 70/20/10 convention. `configs/dataset.yaml` was updated
to reference all three splits (`train`, `val`, `test`) for use in later training and evaluation
scripts.

## Verification

Confirmed image and label counts match exactly in the new `test` split (both directories
report the same file count), so no orphaned images or labels resulted from the move.

## Conclusion

Dataset now has a proper 3-way split with a genuinely held-out test set. Ready for Day 5:
baseline YOLO training.