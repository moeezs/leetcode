# Last updated: 05/06/2025, 22:13:58
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        def hash(num):
            return num % 11

        unique = [[],[],[],[],[],[],[],[],[],[],[]]

        for i in range(len(nums)):
            hashInd = hash(nums[i])
            if nums[i] not in unique[hashInd]:
                unique[hashInd].append(nums[i])
            else:
                return True

        return False