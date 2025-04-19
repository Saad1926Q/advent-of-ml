# Deep ML Problem Sets

This is my list of Leetcode-style ML problem sets from [Deep ML](https://www.deep-ml.com/).


## Problem 1: Matrix × Vector Dot Product
Write a function to compute the dot product between a matrix and a vector.  
If dimensions are mismatched, return `-1`.

## Problem 2: Transpose of a Matrix
Write a function to compute the transpose of a 2D matrix by flipping rows and columns.

## Problem 3: Feature Scaling (Standardization & Min-Max Normalization)
Write a function that takes a NumPy 2D array and returns two scaled versions of it:
- One standardized (Z-score)
- One normalized (Min-Max)  
Round all results to 4 decimal places.

## Problem 4: Single Neuron with Backpropagation

Simulate a single neuron with **sigmoid activation** and implement **backpropagation** to update weights and bias using **gradient descent** for training. Return the updated weights, bias, and MSE loss over epochs.

## Problem 5: K-Fold Cross-Validation  
Implement a function to generate train and test splits for K-Fold Cross-Validation.  
Your task is to divide the dataset into `k` folds and return a list of train-test indices for each fold.

## Problem 6: Precision Metric

Implement a function `precision` that calculates the precision metric given two NumPy arrays: `y_true` and `y_pred`.
Precision is defined as the ratio of true positives (TP) to the sum of true positives and false positives (FP)
