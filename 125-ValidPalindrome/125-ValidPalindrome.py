# Last updated: 7/1/2025, 4:53:46 PM
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 0
        j = len(s) - 1
        accepted = 'qwertyuiopasdfghjklzxcvbnm1234567890'

        while i < j:
            if s[i].lower() not in accepted:
                i += 1
                continue
            if s[j].lower() not in accepted:
                j -= 1
                continue
            if s[i].lower() != s[j].lower():
                return False
            else:
                i += 1
                j -= 1
        return True
        

        
        