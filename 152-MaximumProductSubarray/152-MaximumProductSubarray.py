# Last updated: 1/12/2026, 1:38:57 PM
1class Solution:
2    def maxProduct(self, nums: List[int]) -> int:
3
4        result = float('-inf')
5
6        for i in range(len(nums)):
7            temp = nums[i]
8            if temp > result:
9                    result = temp
10            for j in range(i + 1, len(nums)):
11                temp = temp * nums[j]
12                if temp > result:
13                    result = temp
14        return result
15
16        