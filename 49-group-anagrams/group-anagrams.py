class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        def createCount(s):
            count = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            for char in s:
                count[ord(char) - 97] += 1
            return count
        
        check = {}
        
        for string in strs:
            countGet = createCount(string)
            count = str(countGet)
            if count in check:
                check[count].append(string)
            else:
                check[count] = [string]
        
        returnThing = []
        for key in check:
            returnThing.append(check[key])
        
        return returnThing


        