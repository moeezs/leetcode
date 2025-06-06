# Last updated: 05/06/2025, 22:14:10
class Solution:
    def romanToInt(self, s: str) -> int:

        number = 0

        for i in range(len(s)):
            if len(s) == 1:
                if s[i] == 'I':
                    number += 1
                elif s[i] == 'V':
                    number += 5
                elif s[i] == 'X':
                    number += 10
                elif s[i] == 'L':
                    number += 50
                elif s[i] == 'C':
                    number += 100
                elif s[i] == 'D':
                    number += 500
                elif s[i] == 'M':
                    number += 1000
            elif i == 0:
                if s[i] == 'I' and s[i + 1] == 'V':
                    number += 4
                elif s[i] == 'I' and s[i + 1] == 'X':
                    number += 9
                elif s[i] == 'X' and s[i + 1] == 'L':
                    number += 40
                elif s[i] == 'X' and s[i + 1] == 'C':
                    number += 90
                elif s[i] == 'C' and s[i + 1] == 'D':
                    number += 400
                elif s[i] == 'C' and s[i + 1] == 'M':
                    number += 900
                elif s[i] == 'I':
                    number += 1
                elif s[i] == 'V':
                    number += 5
                elif s[i] == 'X':
                    number += 10
                elif s[i] == 'L':
                    number += 50
                elif s[i] == 'C':
                    number += 100
                elif s[i] == 'D':
                    number += 500
                elif s[i] == 'M':
                    number += 1000
            elif i != len(s) - 1:
                if s[i] == 'V' and s[i - 1] == 'I':
                    continue
                elif s[i] == 'X' and s[i - 1] == 'I':
                    continue
                elif s[i] == 'L' and s[i - 1] == 'X':
                    continue
                elif s[i] == 'C' and s[i - 1] == 'X':
                    continue
                elif s[i] == 'D' and s[i - 1] == 'C':
                    continue
                elif s[i] == 'M' and s[i - 1] == 'C':
                    continue
                elif s[i] == 'I' and s[i + 1] == 'V':
                    number += 4
                elif s[i] == 'I' and s[i + 1] == 'X':
                    number += 9
                elif s[i] == 'X' and s[i + 1] == 'L':
                    number += 40
                elif s[i] == 'X' and s[i + 1] == 'C':
                    number += 90
                elif s[i] == 'C' and s[i + 1] == 'D':
                    number += 400
                elif s[i] == 'C' and s[i + 1] == 'M':
                    number += 900
                elif s[i] == 'I':
                    number += 1
                elif s[i] == 'V':
                    number += 5
                elif s[i] == 'X':
                    number += 10
                elif s[i] == 'L':
                    number += 50
                elif s[i] == 'C':
                    number += 100
                elif s[i] == 'D':
                    number += 500
                elif s[i] == 'M':
                    number += 1000
            elif i == len(s) - 1:
                if s[i] == 'V' and s[i - 1] == 'I':
                    continue
                elif s[i] == 'X' and s[i - 1] == 'I':
                    continue
                elif s[i] == 'L' and s[i - 1] == 'X':
                    continue
                elif s[i] == 'C' and s[i - 1] == 'X':
                    continue
                elif s[i] == 'D' and s[i - 1] == 'C':
                    continue
                elif s[i] == 'M' and s[i - 1] == 'C':
                    continue
                elif s[i] == 'I':
                    number += 1
                elif s[i] == 'V':
                    number += 5
                elif s[i] == 'X':
                    number += 10
                elif s[i] == 'L':
                    number += 50
                elif s[i] == 'C':
                    number += 100
                elif s[i] == 'D':
                    number += 500
                elif s[i] == 'M':
                    number += 1000


        return number