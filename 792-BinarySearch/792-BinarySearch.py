# Last updated: 12/28/2025, 6:31:04 PM
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        high = len(nums) - 1
        low = 0
        

        while low <= high:
            mid = (low + high) / 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return -1