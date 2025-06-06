# Last updated: 05/06/2025, 22:13:54
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []

        for i in range(n):
            i = i + 1
            if i % 15 == 0:
                answer.append('FizzBuzz')
            elif i % 3 == 0:
                answer.append('Fizz')
            elif i % 5 == 0:
                answer.append('Buzz')
            else:
                answer.append(str(i))

        return answer