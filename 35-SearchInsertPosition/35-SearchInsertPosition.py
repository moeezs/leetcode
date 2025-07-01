# Last updated: 6/30/2025, 10:47:58 PM
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums) - 1

        while lo < hi:
            mid = (hi + lo) // 2
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid
        
        if target > nums[len(nums) - 1]:
            return len(nums)
        else:
            return lo