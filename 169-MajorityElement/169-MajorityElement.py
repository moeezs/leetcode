# Last updated: 8/6/2025, 12:21:54 PM
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cache = {}
        for i in range(len(nums)):
            if nums[i] in cache:
                cache[nums[i]] += 1
            else:
                cache[nums[i]] = 1
        print(cache)
        
        top_key = None
        top_value = float('-inf')

        for num in cache:
            if cache[num] > top_value:
                top_value = cache[num]
                top_key = num

        return top_key
        