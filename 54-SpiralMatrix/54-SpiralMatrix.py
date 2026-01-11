# Last updated: 1/10/2026, 11:25:45 PM
1class Solution:
2    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
3        result = []
4        min_n = 0
5        min_m = 0
6        m = len(matrix)
7        n = len(matrix[0])
8        curr_n = 0
9        curr_m = 0
10
11        curr_d = "r"
12
13        while len(result) < len(matrix) * len(matrix[0]):
14            result.append(matrix[curr_m][curr_n])
15            if curr_d == "r":
16                if curr_n < n - 1:
17                    curr_n += 1
18                else:
19                    curr_d = "d"
20                    curr_m += 1
21                    min_m += 1
22                    n -= 1
23            elif curr_d == "d":
24                if curr_m < m - 1:
25                    curr_m += 1
26                else:
27                    curr_d = "l"
28                    curr_n -= 1
29                    m -= 1
30            elif curr_d == "l":
31                if curr_n > min_n:
32                    curr_n -= 1
33                else:
34                    curr_d = "u"
35                    min_n += 1
36                    curr_m -= 1
37            elif curr_d == "u":
38                if curr_m > min_m:
39                    curr_m -= 1
40                else:
41                    curr_d = "r"
42                    curr_n += 1
43        return result
44
45
46        
47