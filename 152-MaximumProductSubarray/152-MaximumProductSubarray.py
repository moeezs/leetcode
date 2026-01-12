# Last updated: 1/12/2026, 1:37:14 PM
1class Solution:
2    def maxProduct(self, nums: List[int]) -> int:
3        if len(nums) == 1:
4            return nums[0]
5
6        result = float('-inf')
7
8        for i in range(len(nums)):
9            temp = nums[i]
10            if temp > result:
11                    result = temp
12            for j in range(i + 1, len(nums)):
13                temp = temp * nums[j]
14                if temp > result:
15                    result = temp
16        return result
17
18        