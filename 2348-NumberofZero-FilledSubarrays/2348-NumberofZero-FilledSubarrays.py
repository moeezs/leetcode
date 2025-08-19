# Last updated: 8/19/2025, 11:02:05 AM
class Solution(object):
    def zeroFilledSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        current_count = 0
        
        for num in nums:
            if num == 0:
                current_count += 1 
                count += current_count
            elif num != 0:
                current_count = 0
            
        return count
        