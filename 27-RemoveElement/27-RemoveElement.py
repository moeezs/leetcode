# Last updated: 05/06/2025, 22:14:09
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = 9999997654321
        
        count = 0
        
        for i in range(len(nums)):
            if nums[i] != 9999997654321:
                count += 1

        for i in range(len(nums)):
            for j in range(len(nums) - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        
        print(nums, count)

        return count