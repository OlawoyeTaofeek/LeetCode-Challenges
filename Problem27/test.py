class Solution:
    def RemoveElement(self, nums: list[int], val: int) -> int:
        a = 0
        new_list = []
        for i in range(0, len(nums)):
            if nums[i] != val:
                a = a+1
                new_list.append(nums[i])
            else:
                pass
        return a, new_list

# print(Solution().RemoveElement(nums = [3,2,2,3], val = 3))
# print(Solution().RemoveElement(nums = [0,1,2,2,3,0,4,2], val = 2))


class Solution2:
    def removeElement(self, nums: list[int], val: int) -> int:
        new_list = []
        index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                new_list.append(nums[index])
                index += 1
        return index, new_list, nums
print(Solution2().removeElement(nums = [3,2,2,3], val = 3))
print(Solution2().removeElement(nums = [0,1,2,2,3,0,4,2], val = 2))
