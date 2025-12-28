# Last updated: 12/28/2025, 6:31:14 PM
import heapq
class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        stones = [-x for x in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            first = -heapq.heappop(stones)
            second = -heapq.heappop(stones)
            if first != second:
                heapq.heappush(stones, -(first - second))
            
        if stones:
            return -stones[0]
        return 0
                



        