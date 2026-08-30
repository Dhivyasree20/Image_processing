# Day 5 Deliverable: Baseline YOLO Training

**Project:** Cow Image Processing & Health Assessment using YOLO
**Date:** Day 5

## Method

Trained a YOLO26n (nano) model from pre-trained weights on the cleaned, split dataset
(542 train / 153 valid images) using `src/train.py`.

**Configuration:**
- Model: yolo26n.pt (pre-trained, fine-tuned on 2 classes)
- Epochs: 50, image size: 640x640, batch size: 16, early-stop patience: 20
- Hardware: Tesla T4 GPU (Google Colab, free tier)
- Training time: ~10-11 minutes (0.177 hours)

## Result (validation set, 153 images / 1,834 instances)

| Metric | Overall | Lying | Standing |
|--------|---------|-------|----------|
| Precision | 0.873 | 0.877 | 0.868 |
| Recall | 0.859 | 0.896 | 0.821 |
| mAP50 | 0.927 | 0.946 | 0.907 |
| mAP50-95 | 0.731 | 0.748 | 0.714 |

## Interpretation

- Strong baseline result: 92.7% mAP50 overall is a solid first-pass score for a nano model on
  ~540 training images.
- The Standing class scores consistently ~4 points lower than Lying across all metrics,
  matching the class imbalance flagged in the Day 2 audit (train set was 62% Lying / 38%
  Standing). The model has simply seen fewer Standing examples. Worth monitoring on the
  held-out test set (Day 7) and considering as a target for improvement on Day 6.
- Training and validation loss both decreased steadily and smoothly across all 50 epochs with
  no signs of instability or overfitting collapse — the run did not trigger early stopping
  (patience=20), meaning the model was still improving, if slowly, through epoch 50.

## Operational note

Two earlier training attempts were lost to free-tier Colab runtime disconnects before
completion. Fixed by changing `train.py` to save training output directly to Google Drive
(`project=` parameter) rather than Colab's temporary local disk, so any completed epochs
persist even through a disconnect. This run completed cleanly with the fix in place.

## Artifacts

- `best.pt` (5.4MB) — best-performing checkpoint, stored in Google Drive
  (`Image_processing_backup/runs/detect/baseline/weights/best.pt`), not committed to git due
  to binary size; referenced here for traceability.
- `last.pt` — final-epoch checkpoint, same location.

## Conclusion

Baseline training successful and reproducible. Ready for Day 6 (attempt to improve on this
baseline) and Day 7 (final evaluation on the held-out test set).