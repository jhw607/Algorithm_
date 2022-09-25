n = int(input())
ropes = [int(input()) for _ in range(n)]
# print(ropes)
ans = 0
# ropes.sort()
for i, rope in enumerate(ropes):
    tmp = max(tmp, rope*(n - i))

print(ans)