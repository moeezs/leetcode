# Last updated: 8/9/2025, 9:47:48 PM
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_str = ''
        temp = ''
        str_lookup = set()
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[j] not in str_lookup:
                    temp += s[i]
                    str_lookup.add(s[j])
                elif s[j] in str_lookup:
                    if len(temp) > len(max_str):
                        max_str = temp
                    temp = ''
                    str_lookup.clear()
                    break

        if len(temp) > len(max_str):
            max_str = temp

        return len(max_str)
