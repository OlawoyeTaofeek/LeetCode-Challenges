# Method 1
# Time complexity: O(n^2)
def MaxProduct(arr) -> int:
    
    if len(arr) < 2:
        return 'No pairs existed'
    a, b = arr[0], arr[1]
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] * arr[j] > a * b:
                a, b = arr[i], arr[j]
    return a * b  


# print(MaxProduct([-1, -3, -4, 2, 0, -5]))

# Method 2:
# Time complexity: O(nlogn)
def maxProduct(arr):
    arr.sort()
    maxproduct = 0
    sum1 = arr[-1] * arr[-2]
    sum2 = arr[0] * arr[1]
    if sum1 > sum2:
        maxproduct = sum1
    else:
        maxproduct = sum2
        
    return maxproduct


# print(maxProduct([-1, -3, -4, 2, 0, -5]))

# print(maxProduct([-1, -3, -4, 2, 0, -5, -9, 7, 12, -12, 15, 1, 23, 18]))

# Time complexity: O(n^2)
def MaxProductOfTwoNumbers(arr):
    i, j, product = 0, 1, arr[0] * arr[1]
    arr.sort()
    while i < len(arr) and j < len(arr):
        result = arr[i] * arr[j]
        if result > product:
            product = result
            
        i += 1
        j += 1
    return product

# print(MaxProductOfTwoNumbers([-1, -3, -4, 2, 0, -5]))
# print(maxProduct([-1, -3, -4, 2, 0, -5, -9, 7, 12, -12, 15, 1, 23, 18]))


#Method 4
# Time complexity: O(n)
def MaxProductOfTwoNumber2(arr):
    max_positive_value , sec_max_positive_value = 0, 0
    
    max_negative_value, sec_max_negative_value = 0, 0
    
    for i in range(len(arr)):
        if arr[i] > max_positive_value:
            sec_max_positive_value = max_positive_value
            max_positive_value = arr[i]
        elif arr[i] > sec_max_positive_value:
            sec_max_positive_value = arr[i]
            
        # Update minimum and second
        # minimum if needed
        if (arr[i] < 0 and abs(arr[i]) > abs(max_negative_value)):
            sec_max_negative_value = max_negative_value
            max_negative_value = arr[i]
        elif (arr[i] < 0 and abs(arr[i]) > abs(sec_max_negative_value)):
            sec_max_negative_value = max_negative_value
            sec_max_negative_value = arr[i]
            
    sum1 = max_negative_value * sec_max_negative_value  
    sum2 = max_positive_value * sec_max_positive_value
    if sum1  > sum2:
        return sum1
    else:
        return sum2
        
print(MaxProductOfTwoNumber2([-1, -3, -4, 2, 0, -5]))    
print(MaxProductOfTwoNumber2([-1, -3, -4, 2, 0, -5, -9, 7, 12, -12, 15, 1, 23, 18]))


# Middle Function
# Write a function called middle that takes a list and returns a new list that contains all but the first and last elements.
def middle(lst):
    n = len(lst)
    new_list = lst[-n+1:-1]
    return new_list

# print(middle([1, 2, 3, 4]))

def middle2(lst):
    n = len(lst)
    new_list = lst[1:n-1]
    return new_list
# print(middle2([1, 2, 3, 4]))


def middle3(lst):
    new = lst[1:]
    del new[-1]
    return new
print(middle3([1, 2, 3, 4]))


# 2D Lists

#Given 2D list calculate the sum of diagonal elements.

# Example

myList2D= [[1,2,3],[4,5,6],[7,8,9]] 
 
# sumDiagonal(myList2D) # 15

def sumDiagonal(arr):
    # TODO
    i = 0
    diagonal_sum = arr[i][i] + arr[i+1][i+1] + arr[i+2][i+2]
    return diagonal_sum

def sumDiagonal2(arr):
    sum = 0
    i = 0
    while i < len(arr):
        sum = sum + arr[i][i]
        i += 1
    return sum

# print(sumDiagonal2([[1,2,3],[4,5,6],[7,8,9]]))

def sumDiagonal3(arr):
    sum = 0
    for i in range(len(arr)):
        sum = sum + arr[i][i]
    return sum

print(sumDiagonal3([[1,2,3,4],[5,6,7,8],[9,10,11,12], [13,14,15,16]]))
        

