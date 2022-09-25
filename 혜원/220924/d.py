from collections import defaultdict

# arr = defaultdict(list)

# arr[1] = [0,1]
# arr[2].append(2)

# print(arr)
# print(arr[3])
# if not arr[3]:
#     print('yes')
# else:
#     print('no')
a = [[4,1000],[6,1000],[21,3000],[16,2000]]

a.sort(key=lambda x: -x[0])
print(a)
a.sort(key=lambda x: x[1])
print(a)


solution.py
2022-09-24 12:29:31
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
from typing import List
from collections import deque

def solution(n: int, m: int, fires: List[List[int]], ices: List[List[int]]) -> List[List[int]]:
    answer = [[]]

    map = [[0]*n]*n
    que_fire = deque(fires)
    que_ice = deque(ices)

    dx = [-1, 1, 0, 0] # 상하좌우
    dy = [0, 0, -1, 1]

    s=1

    while s<=m:

        for fire in fires:
            fire_x, fire_y = fire





    return answer



