# Last updated: 12/28/2025, 6:30:53 PM
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
        