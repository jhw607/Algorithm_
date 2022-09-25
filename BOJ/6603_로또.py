
from itertools import combinations

nums = input()
answer = [[]]
s = []

while True:
    if nums == '0': break
    s.append(list(nums[2:].split(' ')))
    nums = input()



n = len(s)

for i in range(n):

    answer = list(map(list, combinations(s[i], 6)))
    # print(answer)
    for ans in answer:
        ans = list(map(int, ans))
        ans.sort()
        print(*ans)

    print()

# while input != 0:
#     print("1")
#     s = list(map(int, input.split('')))
#     print("2")
#     k = s.pop(0)
#     # answer = list(combinations(s, 6))
#     print(s)


