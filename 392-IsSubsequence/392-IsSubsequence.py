# Last updated: 8/7/2025, 12:48:58 PM
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sub = 0
        iterate = 0

        while iterate < len(t):
            if sub == (len(s)):
                return True
            if s[sub] == t[iterate]:
                sub += 1
                iterate += 1
            else:
                iterate += 1

        if sub == (len(s)):
            return True
        else:
            return False

            
        