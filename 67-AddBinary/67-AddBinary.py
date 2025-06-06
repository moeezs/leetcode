# Last updated: 05/06/2025, 22:14:03
class Solution:
    def addBinary(self, a: str, b: str) -> str:

        numa = 0
        numb = 0

        if a == '0' and b == '0':
            return '0'

        for i, num in enumerate(a):
            if num == '1':
                numa += 2 ** (len(a) - 1 - i)
            else:
                continue
        
        for i, num in enumerate(b):
            if num == '1':
                numb += 2 ** (len(b) - 1 - i)
            else:
                continue
        
        binnum = bin(numa + numb)

        return str(binnum).lstrip('0b')
        