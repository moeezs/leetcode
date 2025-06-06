# Last updated: 05/06/2025, 22:14:13
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        two_num = []

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    if nums[i] + nums[j] == target:
                        two_num.append(i)
                        two_num.append(j)
                        return(two_num)