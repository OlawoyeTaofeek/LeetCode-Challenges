import numpy as np


# Method 1
def rotateMatrix(matrix):
    check = True
    n = len(matrix)
    for i in range(len(matrix)):
        if not (len(matrix[i]) == n):
            check = False
    if not (n >= 1 or n<= 20):
        check = False
    for i in range(len(matrix)):
        for j in range(n):
            if not (-1000 <= matrix[i][j]  or matrix[i][j] <= 1000):
                check = False
                
    if check:
        for layer in range(int(n / 2)):
            first = layer
            last = n - layer - 1
            for i in range(first, last):
                top = matrix[layer][i]
                matrix[layer][i] = matrix[- i - 1][layer]
                matrix[-i - 1][layer] = matrix[- layer - 1][- i - 1]
                matrix[- layer - 1][- i - 1] = matrix[i][- layer - 1]
                matrix[i][- layer - 1] = top
        return matrix


# Method 2
def rotateMatrix2(matrix):
    check = True
    n = len(matrix)
    for i in range(len(matrix)):
        if not (len(matrix[i]) == n):
            check = False
    if not (n >= 1 or n<= 20):
        check = False
    for i in range(len(matrix)):
        for j in range(n):
            if not (-1000 <= matrix[i][j]  or matrix[i][j] <= 1000):
                check = False
    
    if check:
        
        for r in range(len(matrix)):
            for c in range(r):
                matrix[r][c],  matrix[c][r] = matrix[c][r], matrix[r][c]
                
        for row in matrix:
            row[:] = row[::-1]
            
        return matrix

    
# Method 3:
def rotateMatrix3(matrix):
    n = len(matrix)
    for r in range(len(matrix)):
        for c in range(r):
            matrix[r][c],  matrix[c][r] = matrix[c][r], matrix[r][c]
    for i in range(n):
        for j in range(int(n/2)):
            temp = matrix[i][j]
            matrix[i][j] = matrix[i][n-j-1]
            matrix[i][n-j-1] = temp
    return matrix


# Method 4:

def rotateMatrix4(matrix):
    matrix = matrix.transpose()
    for row in matrix:
        row[:] = row[::-1]
        
    return matrix
    

matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(rotateMatrix4(matrix))

matrix2 = np.array([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])
print(rotateMatrix4(matrix2))

# matrix3 = np.array([[0, 1], [1, 0]])
# print(rotateMatrix(matrix3))

# matrix4 = np.array([[0, 0, 0], [0, 1, 0], [1,1,1]])
# print(rotateMatrix(matrix4))