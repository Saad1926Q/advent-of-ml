"""
Feature Scaling Implementation

Write a Python function that performs feature scaling on a dataset using both standardization and min-max normalization. The function should take a 2D NumPy array as input, where each row represents a data sample and each column represents a feature. It should return two 2D NumPy arrays: one scaled by standardization and one by min-max normalization. Make sure all results are rounded to the nearest 4th decimal.

Example:
Input:
data = np.array([[1, 2], [3, 4], [5, 6]])
Output:
([[-1.2247, -1.2247], [0.0, 0.0], [1.2247, 1.2247]], [[0.0, 0.0], [0.5, 0.5], [1.0, 1.0]])

"""


import numpy as np

def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
    mean=np.mean(data,axis=0)
    std=np.std(data,axis=0)
    standardized_data=(data-mean)/std
    min_features=np.min(data,axis=0)
    max_features=np.max(data,axis=0)
    normalized_data=(data-min_features)/(max_features-min_features)

    return standardized_data, normalized_data


print(feature_scaling(np.array([[1, 2], [3, 4], [5, 6]])))