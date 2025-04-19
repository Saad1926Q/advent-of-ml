"""
Implement Precision Metric

Write a Python function precision that calculates the precision metric given two numpy arrays: y_true and y_pred. 
The y_true array contains the true binary labels, and the y_pred array contains the predicted binary labels. 
Precision is defined as the ratio of true positives to the sum of true positives and false positives.

Example:
Input:
import numpy as np

y_true = np.array([1, 0, 1, 1, 0, 1])
y_pred = np.array([1, 0, 1, 0, 0, 1])

result = precision(y_true, y_pred)
print(result)
Output:
1.0

Reasoning:
True Positives (TP) = 3
False Positives (FP) = 0
Precision = TP / (TP + FP) = 3 / (3 + 0) = 1.0

"""

import numpy as np


def precision(y_true, y_pred):
	TP=0
	FP=0
	positives_idx=np.arange(len(y_pred))[y_pred==np.ones(len(y_pred))]
	positives_mask=y_pred[positives_idx]==y_true[positives_idx]
	TP=len(positives_idx[positives_mask])
	FP=len(positives_idx[~positives_mask])
	return TP/(FP+TP)

precision(y_true = np.array([1, 0, 1, 1, 0, 1]),y_pred = np.array([1, 0, 1, 0, 0, 1]))