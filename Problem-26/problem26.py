import array


def removeDuplicate(lists):
    array_without_duplicate = []
    for num in lists:
        if num in array_without_duplicate:
            pass
        else:
            array_without_duplicate.append(num)
    print(array_without_duplicate)
    return len(array_without_duplicate)


print(removeDuplicate([0,0,1,1,1,2,2,3,3,4]))
print(removeDuplicate([1,1,2]))


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        check = True
        if not(len(nums) >= 1 or len(nums) <= (3 * 10**4)):
            check = False
        for i in range(len(nums)):
            if not(nums[i] >= -100 or nums[i] <= 100):
                check = False
        array_without_duplicate = []
        if check:    
            for num in nums:
                if num in array_without_duplicate:
                    pass
                else:
                    array_without_duplicate.append(num)
            print(array_without_duplicate)
            return len(array_without_duplicate)
    
# print(Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
# print(Solution().removeDuplicates([1,1,2]))

class Solution1:
    def removeDuplicates(self, nums: list[int]) -> int:
        unique_nums = set(nums)
        return len(unique_nums)
    
# print(Solution1().removeDuplicates([0,0,1,1,1,2,2,3,3,4]))


class Solution2:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0
        a = 0
        for i in range(1, len(nums)):
            if  nums[a] != nums[i]:
                a = a + 1
                nums[a] = nums[i] 
        k = a + 1  
        return k
                
                
print(Solution2().removeDuplicates([0,0,1,1,1,2,2,3,3,4]))     
print(Solution2().removeDuplicates([1,1,2]))


