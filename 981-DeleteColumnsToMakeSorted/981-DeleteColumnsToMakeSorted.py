# Last updated: 12/28/2025, 6:30:57 PM
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:

        remo = 0

        for i in range(len(strs[0])):
            col = []
            for j in range(len(strs)):
                col.append(strs[j][i])
            if sorted(col) != col:
                remo += 1

        return remo