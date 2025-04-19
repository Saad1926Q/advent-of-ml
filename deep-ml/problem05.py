"""
Implement K-Fold Cross-Validation

Implement a function to generate train and test splits for K-Fold Cross-Validation.
Your task is to divide the dataset into k folds and return a list of train-test indices for each fold.

Example:
Input:
k_fold_cross_validation(np.array([0,1,2,3,4,5,6,7,8,9]), np.array([0,1,2,3,4,5,6,7,8,9]), k=5, shuffle=False)
Output:
[([2, 3, 4, 5, 6, 7, 8, 9], [0, 1]), ([0, 1, 4, 5, 6, 7, 8, 9], [2, 3]), ([0, 1, 2, 3, 6, 7, 8, 9], [4, 5]), ([0, 1, 2, 3, 4, 5, 8, 9], [6, 7]), ([0, 1, 2, 3, 4, 5, 6, 7], [8, 9])]

"""


import numpy as np

def k_fold_cross_validation(X: np.ndarray, y: np.ndarray, k=5, shuffle=True, random_seed=None):
    """
    Implement k-fold cross-validation by returning train-test indices.
    """

    result=[]
    if random_seed is not None:
        np.random.seed(random_seed)
    

    if shuffle==True:
        np.random.shuffle(X)

    folds=np.array(np.split(X,k))



    for i in range(k):
        mask=np.arange(len(folds))!=i
        test=folds[i]
        train=folds[mask].flatten()
        result.append((train,test))



    return result


