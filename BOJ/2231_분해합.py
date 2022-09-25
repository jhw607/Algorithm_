
n = input()
num = int(n)
answer = 0

for i in range(num):
    nums = list(map(int, str(i)))
    if sum(nums) + i == num:
        answer = i
        break
else:
    answer = 0

print(answer)