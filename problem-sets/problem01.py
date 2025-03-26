'''

Matrix times Vector
Write a Python function that takes the dot product of a matrix and a vector. return -1 if the matrix could not be dotted with the vector

Example:
Input:
a = [[1,2],[2,4]], b = [1,2]
Output:
[5, 10]
Reasoning:
1*1 + 2*2 = 5; 1*2+ 2*4 = 10

'''


def matrix_dot_vector(a:list[list[int|float]],b:list[int|float])-> list[int|float]:
    result=[]
    for vector in a:
        smth=0
        if len(vector)!=len(b):
            return -1
        for i,element in enumerate(vector):
            smth+=element*b[i]
        result.append(smth)

    return result

	

	
print(matrix_dot_vector([[1,2],[2,4,6]],[1,2]))