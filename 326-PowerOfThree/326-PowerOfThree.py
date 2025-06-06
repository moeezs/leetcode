# Last updated: 05/06/2025, 22:13:56
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        num = 1
        for i in range(100):
            if num == n:
                return True
            num = num * 3
        
        return False