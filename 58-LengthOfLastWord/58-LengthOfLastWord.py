# Last updated: 05/06/2025, 22:14:05
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip()
        count = 0
        spacecount = 0

        for i in range(len(s)):
            if s[i] == ' ':
                spacecount += 1
        
        print(spacecount)

        if spacecount > 0:
            for i in reversed(range(len(s))):
                if s[i] != ' ':
                    count += 1
                else:
                    return count
        else:
            return len(s)