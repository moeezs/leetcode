# Last updated: 8/19/2025, 11:00:12 AM
class Solution(object):
    def zeroFilledSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        current_count = 0

        # for i in range(len(nums)):
        #     print(nums[i])
        #     if nums[i] == 0:
        #         print(nums[i])
        #         if current_count != 0:
        #             current_count += 1 
        #             count += current_count
        #         elif current_count == 0:
        #             current_count += 1
        #             count += 1
        #     elif nums[i] != 0:
        #         if current_count != 0:
        #             current_count = 0
        for num in nums:
            if num == 0:
                if current_count != 0:
                    current_count += 1 
                    count += current_count
                elif current_count == 0:
                    current_count += 1
                    count += 1
            elif num != 0:
                if current_count != 0:
                    current_count = 0
            
        return count
        