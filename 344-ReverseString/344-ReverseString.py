# Last updated: 05/06/2025, 22:13:52
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = s[::-1]
        s.clear()
        
        for letter in n:
            s.append(letter)