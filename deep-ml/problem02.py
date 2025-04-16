
'''
Transpose of a Matrix
Write a Python function that computes the transpose of a given matrix.

Example:
Input:
a = [[1,2,3],[4,5,6]]
Output:
[[1,4],[2,5],[3,6]]
Reasoning:
The transpose of a matrix is obtained by flipping rows and columns.

'''

def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    T=[]
    c=len(a[0])
    r=len(a)

    for i in range(c):
        T.append([])

    for vector in a:
        for col,value in enumerate(vector):
            T[col].append(value)

    return T

print(transpose_matrix([[1,2,3],[4,5,6]]))

