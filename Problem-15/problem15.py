import numpy as np


# Correct Solution but time consuming
# Time complexity of O(n^3)
def threeSum(nums):
    lst = [] 
    lst2 = []
    for i in range(len(nums)):
        for j in range(1, len(nums)):
            for k in range(2, len(nums)):
                if i != j and i != k and j != k:
                    if nums[i] + nums[j] + nums[k] == 0:
                        lst.append([nums[i], nums[j], nums[k]])
    for i in lst:
        i.sort()
        if i not in lst2:
            lst2.append(i)
        else:
            continue
    return lst2
        



# print(threeSum(nums = [-1,0,1,2,-1,-4]))
# print(threeSum(nums = [0,0,0]))
print(threeSum(nums = [4,-10,-11,-12,-8,-12,-14,-11,-6,2,-4,2,3,12,-3,-12,-14,-12,-8,-9,-6,-3,10,2,14,10,7,-7,-9,0,-9,10,-2,-5,14,5,-9,7,9,0,-14,12,10,4,9,-8,8,11,-5,-15,-13,-3,-11,4,14,11,-1,-2,-11,5,14,-4,-8,-3,6,-9,9,12,6,3,-10,7,0,-15,-3,-13,-8,12,13,-5,12,-15,7,8,-4,-2,4,2,3,9,-8,2,-10,-1,6,3,-2,0,-7,11,-12,-2,3,-4,-2,7,-2,-3,4,-12,-1,1,10,13,-5,-9,-12,6,8,7,0,7,-6,5,13,8,-14,-12]))

# Using Two Pointer Algorithm
