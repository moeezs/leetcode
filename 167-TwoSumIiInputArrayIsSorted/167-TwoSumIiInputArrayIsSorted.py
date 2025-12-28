# Last updated: 12/28/2025, 6:31:24 PM
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        numbers_lookup = set(numbers)
        end = len(numbers) - 1
        result = []
        
        # if (target > 0):
        #     while numbers[end] > target:
        #         end -= 1
        # else:
        #     while numbers[end] < target:
        #         end -= 1
            
        while end != 0:
            if (target - numbers[end]) in numbers_lookup:
                result.append(end + 1)
                break
            else:
                end -= 1
        
        find = target - numbers[end]
        for i in range(end):
            if numbers[i] == find:
                result.append(i + 1)
                break
        
        result[0], result[1] = result[1], result[0]

        return result




        