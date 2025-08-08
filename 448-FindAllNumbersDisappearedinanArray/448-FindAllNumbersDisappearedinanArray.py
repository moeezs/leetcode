# Last updated: 8/8/2025, 11:07:29 AM
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        nums_lookup = set(nums)
        for i in range(1, len(nums)+1):
            if i not in nums_lookup:
                result.append(i)
        
        return result

        