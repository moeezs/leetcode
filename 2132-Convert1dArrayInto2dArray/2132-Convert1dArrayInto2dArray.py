# Last updated: 12/28/2025, 6:30:56 PM
class Solution(object):
    def construct2DArray(self, original, m, n):
        """
        :type original: List[int]
        :type m: int
        :type n: int
        :rtype: List[List[int]]
        """
        check_help = float(len(original) / float(m))
        if (check_help / float(n)) != 1:
            return []
        
        i = 0
        n_help = 0
        result = []
        temp = []

        while i < len(original):
            if n_help < n:
                temp.append(original[i])
                n_help += 1
            elif n_help == n:
                result.append(temp)
                temp = [original[i]]
                n_help = 1
            i += 1
        
        if temp:
            result.append(temp)


        return result

        