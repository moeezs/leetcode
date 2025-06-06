# Last updated: 05/06/2025, 22:13:52
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:

        strn = ''

        newlist = []

        for digit in num:
            strn += str(digit)
        
        intn = int(strn) + k

        strn = str(intn)

        for letter in strn:
            newlist.append(int(letter))

        return newlist