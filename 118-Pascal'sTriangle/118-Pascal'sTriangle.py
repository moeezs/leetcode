# Last updated: 7/24/2025, 9:13:42 PM
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        
        prevRows = self.generate(numRows - 1)
        newRow = [1] * numRows
        
        for i in range(1, numRows - 1):
            newRow[i] = prevRows[-1][i - 1] + prevRows[-1][i]
        
        prevRows.append(newRow)
        return prevRows

        return returnThing

        