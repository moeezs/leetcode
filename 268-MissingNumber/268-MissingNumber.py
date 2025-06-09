# Last updated: 08/06/2025, 21:08:11
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current = 0
        for i in range(len(nums)):
            if current not in nums:
                return current
            current += 1
        return current
        