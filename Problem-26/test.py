# class Solution:
#     def removeDuplicates(self, nums: list[int]) -> int:
#         array_without_duplicate = []

#         for num in nums.sort():
#             if num in array_without_duplicate:
#                 pass
#             else:
#                 array_without_duplicate.append(num)
#         return len(array_without_duplicate)


# print(Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
# print(Solution().removeDuplicates([1,1,2]))

nums =[2,3,4,7,2,1,8,10,6]
print(sorted(nums))



def noDuplicate(mylist, a=0):
    for i in range(1, len(mylist)):
        if mylist[a] != mylist[i]:
            a = a + 1
            mylist[a] = mylist[i]
    k = a + 1
    return k

print(noDuplicate(mylist = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))


# def duplicates(nums):
#     dups = sum(any(nums.count(x) > 1 for x in nums))
#     return dups


def count_duplicates(nums):
    num_counts = {}
    duplicates = 0

    for num in nums:
        if num in num_counts:
            num_counts[num] += 1
            if num_counts[num] == 2:
                duplicates += 1
        else:
            num_counts[num] = 1

    return duplicates

print(count_duplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))


def count_duplicates(nums):
    num_counts = {}

    for num in nums:
        if num in num_counts:
            num_counts[num] += 1
        else:
            num_counts[num] = 1

    unique_elements = [num for num, count in num_counts.items() if count == 1]
    lengths = [count for num, count in num_counts.items()]

    return unique_elements, lengths
print(count_duplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
