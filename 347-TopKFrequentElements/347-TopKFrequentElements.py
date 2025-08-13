# Last updated: 8/12/2025, 8:19:05 PM
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        cache = {}

        for num in nums:
            if num in cache:
                cache[num] += 1
            else:
                cache[num] = 1

        returnThing = []
        items = cache.items()
        items = list(items)
        items.sort(key=lambda pair: pair[1], reverse=True)

        for i in range(k):
            returnThing.append(items[i][0])

        return returnThing

            
        