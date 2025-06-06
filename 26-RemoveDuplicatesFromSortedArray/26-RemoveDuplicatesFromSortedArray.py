# Last updated: 05/06/2025, 22:14:09
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        k = 0
        met = []

        for i in range(len(nums)):
            if nums[i] not in met:
                k += 1
                met.append(nums[i])
            elif nums[i] in met:
                nums[i] = '_'
        
        i = 0
        for j in range(len(nums)):
            if nums[j] != '_':
                nums[i], nums[j] = nums[j], nums[i]
                i += 1

        return k