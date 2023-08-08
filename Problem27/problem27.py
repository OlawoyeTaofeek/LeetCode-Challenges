class Solution:
    def RemoveElement(self, nums: List[int], val: int) -> int:
        a = 0
        new_list = []
        for i in range(0, len(nums)):
            if nums[i] != val:
                a = a+1
                new_list.append(nums[i])
            else:
                pass
        return a, new_list

print(RemoveElement(nums = [3,2,2,3], val = 3))
print(RemoveElement(nums = [0,1,2,2,3,0,4,2], val = 2))
