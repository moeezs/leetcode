# Last updated: 12/28/2025, 6:30:52 PM
class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total_apples = sum(apple)
        capacity.sort(reverse=True)

        need = 0
        while total_apples > 0:
            total_apples -= capacity[need]
            need += 1
        return need