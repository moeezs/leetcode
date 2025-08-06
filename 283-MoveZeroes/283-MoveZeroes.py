# Last updated: 8/6/2025, 11:43:35 AM
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        iterate = 0
        catcher = 1
        i = 0
        count = 0
        while(count < len(nums)):

            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
                
            else:
                i+=1
            count +=1



            

        