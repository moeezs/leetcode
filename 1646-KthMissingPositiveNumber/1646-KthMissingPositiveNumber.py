# Last updated: 05/06/2025, 22:13:55
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        miss_nums = []
        for i in range(10000):
            if arr.count(i+1) > 0:
                continue
            else:
                miss_nums.append(i+1)

        return miss_nums[k-1]
