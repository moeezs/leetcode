# Last updated: 05/06/2025, 22:13:57
class Solution:
    def hammingWeight(self, n: int) -> int:

        count = 0
        for num in str(bin(n)):
            if num == '1':
                count += 1
        
        return count