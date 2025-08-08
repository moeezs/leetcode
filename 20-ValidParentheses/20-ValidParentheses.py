# Last updated: 8/7/2025, 10:01:25 PM
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        coress = {')': '(', ']':'[', '}': '{'}
        opening = '[{('
        closing = ']})'
        stack = []
        for brack in s:
            if brack in opening:
                stack.append(brack)
            else:
                if stack == []:
                    return False
                if coress[brack] == stack[len(stack) - 1]:
                    stack.pop()
                else:
                    return False

        return stack == []
        