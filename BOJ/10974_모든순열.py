from itertools import permutations

n = int(input())

arrs = list(permutations(range(1, n+1)))

for i in range(n-1, -1, -1):
    arrs.sort(key= lambda x : x[i])

[print(*arr) for arr in arrs]