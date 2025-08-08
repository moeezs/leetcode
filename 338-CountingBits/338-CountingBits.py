# Last updated: 8/7/2025, 9:27:50 PM
class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        two_place = 2
        twos = []
        while two_place < n+1:
            twos.append(two_place)
            two_place *= 2

        bottom_two = -1
        result = []
        def get_bit_count(num):
            global bottom_two
            if num == 0:
                return 0
            elif num == 1:
                return 1
            elif num in twos:
                bottom_two = num
                return 1
            else:
                return 1 + result[num - bottom_two]


        for i in range(n + 1):
            result.append(get_bit_count(i))
            
        return result


        