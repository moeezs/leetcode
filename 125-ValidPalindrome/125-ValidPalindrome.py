# Last updated: 05/06/2025, 22:13:59
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
        s_new = ""
        for char in s:
            if char in alph:
                s_new += char.lower()
        print(s_new)
        
        if s_new == s_new[::-1]:
            return True
        else:
            return False
