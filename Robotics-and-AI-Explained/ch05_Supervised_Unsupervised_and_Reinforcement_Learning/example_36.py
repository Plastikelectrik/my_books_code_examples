# Evaluate a defect detector on 1000 products
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score, recall_score

# 20 defects (1) and 980 good products (0)
truth = [1] * 20 + [0] * 980
# the detector finds 15 defects, misses 5,
# and wrongly flags 10 good products
pred = [1] * 15 + [0] * 5 + [1] * 10 + [0] * 970

tn, fp, fn, tp = confusion_matrix(truth, pred).ravel()
print(f"TP={tp} FN={fn} FP={fp} TN={tn}")
print(f"precision: {precision_score(truth, pred):.2f}")
print(f"recall   : {recall_score(truth, pred):.2f}")
acc = (tp + tn) / len(truth)
print(f"accuracy : {acc:.3f}")
