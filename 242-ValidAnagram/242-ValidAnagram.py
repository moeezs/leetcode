# Last updated: 05/06/2025, 22:13:57
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        counter = {}
        counterTwo = {}
        if len(s) != len(t):
            return False
        for char in s:
            if char in counter:
                counter[char] += 1
            else:
                counter[char] = 1

            counterTwo[char] = t.count(char)
        if counter == counterTwo:
            return True
        return False
            
        
        