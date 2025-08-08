# Last updated: 8/8/2025, 9:16:16 AM
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        current_word = ''
        concat = []
        for i in range(len(s)):
            if s[i] != ' ':
                current_word += s[i]
            elif s[i] == ' ':
                if current_word:
                    concat.append(current_word)
                    current_word = ''
            if i == len(s) - 1:
                if current_word:
                    concat.append(current_word)
        
        concat = concat[::-1]
        answer = ''
        for word in concat:
            answer = answer + word + ' '
        
        return answer[:-1]


        