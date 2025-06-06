# Last updated: 05/06/2025, 22:14:04
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        string = ''
        newlist = []

        for num in digits:
            string += str(num)
        
        num = int(string) + 1

        numstr = str(num)

        for num in numstr:
            newlist.append(int(num))

        return newlist