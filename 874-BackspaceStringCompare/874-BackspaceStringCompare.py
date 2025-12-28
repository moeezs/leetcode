# Last updated: 12/28/2025, 6:30:59 PM
class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_new = ""
        t_new = ""
        for i in range(len(s)):
            if s[i] == '#':
                if s_new != "": 
                    s_new = s_new[:-1]
            else: 
                s_new += s[i]
        
        for i in range(len(t)):
            if t[i] == '#':
                if t_new != "": 
                    t_new = t_new[:-1]
            else: 
                t_new += t[i]

        return t_new == s_new
