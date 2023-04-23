import numpy as np

def rotateMatrix(matrix):
    n = len(matrix)
    for layer in range(n//2):
        first = layer
        last = n - layer - 1
        for i in range(first, last):
            top = matrix[layer][i]
            matrix[layer][i] = matrix[-1-i][layer]
            matrix[-1-i][layer] = matrix[-layer-1][-i-1]
            matrix[-layer-1][-i-1] = matrix[i][-layer-1]
            matrix[i][-layer-1] = top
        
    return matrix

# matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(rotateMatrix(matrix))
        

# matrix2 = np.array([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])
# print(len(matrix2))
# print(rotateMatrix(matrix2))
        
matrix3 = np.array([[5,1,9,11,12],[2,4,8,10, 13],[13,3,6,7, 10],[15,14,12,16, 9], [2, 3, 5, 6, 8]])
print(matrix3)
print(rotateMatrix(matrix3))