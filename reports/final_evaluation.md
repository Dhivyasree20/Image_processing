# Day 7 Deliverable: Final Test Set Evaluation

**Project:** Cow Image Processing & Health Assessment using YOLO
**Date:** Day 7

## Method

Ran the Day 6 model (yolo26s, `improved_s` run) against the **test split** (73 images, 878
instances) — created on Day 4 and never used in training or model-selection decisions until
this point. This is a single, one-time evaluation intended to give an honest, unbiased
estimate of real-world performance.

## Result

| Metric | Overall | Lying | Standing |
|--------|---------|-------|----------|
| Precision | 0.889 | 0.892 | 0.885 |
| Recall | 0.927 | 0.935 | 0.918 |
| mAP50 | 0.940 | 0.940 | 0.939 |
| mAP50-95 | 0.743 | 0.742 | 0.745 |

## Comparison to validation results (Day 6)

| Metric | Validation | Test | Gap |
|--------|-----------|------|-----|
| mAP50 | 0.953 | 0.940 | -1.3 pts |
| mAP50-95 | 0.758 | 0.743 | -1.5 pts |
| Precision | 0.915 | 0.889 | -2.6 pts |
| Recall | 0.901 | 0.927 | +2.6 pts |

## Interpretation

**The model generalizes well.** The gap between validation and test performance is small
(1-3 points across metrics), which indicates the model learned genuine, transferable visual
patterns rather than overfitting to the training/validation data. A large drop on the
never-seen test set would have been a red flag; this is not that.

**The class-imbalance concern from Day 2/5 has essentially resolved.** On the final test set,
Lying (mAP50 0.940) and Standing (mAP50 0.939) are almost identical — a 0.001 difference,
compared to a ~4-point gap on the Day 5 nano-model baseline. The larger model (Day 6) appears
to have fully closed this gap in practice.

**Recall (0.927) is notably strong** — the model successfully identifies ~93% of actual
cow/posture instances in unseen images. For a health-screening use case, high recall matters:
missing a cow (false negative) is generally worse than an extra false alarm, since missed
detections mean no screening signal is generated at all for that animal.

## Conclusion

Baseline posture-detection model performance: **mAP50 = 0.940 on held-out test data**, with
balanced performance across both classes and good generalization from training to unseen data.
This is a solid, defensible baseline result for a first-pass internship project.

**Scope reminder (per project doc):** this model detects and classifies posture only
(Standing/Lying). It does not diagnose health or disease. Day 8 will define screening logic
that flags cases for human/SME review based on these detections — not automated diagnosis.

Ready for Day 8: health-screening logic layer.