def func(k, n, comp, ans, depth):
    if depth == k:
        return


k = int(input())
comp = input().split(' ')
nums = [0]*(k+1)

for i, c in enumerate(comp):
    if c == '<':
        nums[i] = 1
        # nums[i] -= 1
    else:
        nums[i] = 0
        # nums[i+1] -= 1
print(nums)
max_num = max(nums)
min_num = min(nums)
n = [0,1,2,3,4,5,6,7,8,9]



# ans1 = []
# ans2 = []
# for i, num in enumerate(nums):
#     if num == 2:
#         ans1.append(n.pop())
#     elif num == 1:
#         ans1.append(n.pop(-2))
#     else:
#         ans1.append(n)