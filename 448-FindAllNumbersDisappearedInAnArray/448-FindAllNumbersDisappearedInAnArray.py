# Last updated: 12/28/2025, 6:31:16 PM
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

        