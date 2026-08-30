# Day 6 Deliverable: Model Improvement Attempt

**Project:** Cow Image Processing & Health Assessment using YOLO
**Date:** Day 6

## Method

Trained a larger model, yolo26s (small, ~10M parameters), as a direct comparison against the
Day 5 baseline (yolo26n, nano, ~2.5M parameters). Identical dataset, splits, and training
settings (50 epochs, imgsz=640, batch=16, patience=20) — model size was the only variable
changed, to isolate its effect.

## Result: yolo26n (Day 5 baseline) vs yolo26s (Day 6)

| Metric | yolo26n | yolo26s | Change |
|--------|---------|---------|--------|
| Overall mAP50 | 0.927 | 0.953 | +2.6 pts |
| Overall mAP50-95 | 0.731 | 0.758 | +2.7 pts |
| Overall Precision | 0.873 | 0.915 | +4.2 pts |
| Overall Recall | 0.859 | 0.901 | +4.2 pts |
| Lying mAP50 | 0.946 | 0.962 | +1.6 pts |
| Standing mAP50 | 0.907 | 0.943 | +3.6 pts |
| Training time | ~10 min | ~15 min | +50% |
| Model file size | 5.4 MB | 20.3 MB | ~4x |

## Interpretation

The larger model improved every single metric, with no signs of overfitting (validation
metrics improved smoothly and consistently across all 50 epochs, mirroring the training loss
trend). Most notably, the **Standing-class gap flagged in the Day 5 report narrowed
substantially** — from a 3.9-point deficit vs Lying (yolo26n) to a 1.9-point deficit
(yolo26s) — suggesting the added model capacity helped it learn the subtler visual cues that
distinguish standing posture.

The trade-off is a ~50% longer training time and a ~4x larger model file. For this project's
scope (baseline research/screening tool, not real-time production deployment), this trade-off
is well worth the accuracy gain.

## Decision

**yolo26s (`improved_s` run) is adopted as the working model going forward**, superseding the
Day 5 `baseline` run. Both sets of weights remain saved in Drive for reference/comparison.

## Conclusion

Model improvement successful — Day 6 goal achieved. Ready for Day 7: final, one-time
evaluation on the held-out test set (created Day 4, never used for training or tuning).