n = int(input())
boxes = list(map(int, input().split(' ')))
arr = [0]*(n+1)
dp = [0]*(n+1)
# arr = [[0]*(n+1), [0]*(n+1)]
# dp = [[0]*(n+1), [0]*(n+1)]
# for i, box in enumerate(boxes):
#     dp.append((box, i))

# dp.sort(key = lambda x:x[0])

# print(dp)


# arr[0] = 1
# for i, d in enumerate(dp,1):
#     box, idx = d
#     if dp[i-1][1] < idx:
#         arr[i] = arr[i-1] + 1
#     else:
#         tmp = i-1
#         while tmp>0:
#             tmp -= 1
#             if boxes[tmp] < box:
#                 break
#         dp[i] = dp[tmp] + 1

# print(dp)
# 0:포함, 1:미포함
arr[0] = 1
for i, box in enumerate(boxes,1):
    
    if boxes[i-1] < box:
        # dp[0][i] = box
        # dp[1][i] = dp[0][i-1]
        dp[i] = box
        # arr[0][i] = max(arr[0][i-1], arr[1][i-1]) + 1
        # arr[1][i] = max(arr[0][i-1], arr[1][i-1])
        arr[i] = arr[i-1]+1

    else:
        tmp = i-1
        while tmp>0:
            tmp -= 1
            if boxes[tmp] < box:
                break
        # arr[i] = arr[tmp] + 1

        # dp[0][i] = dp[0][tmp]
        # dp[1][i] = dp[1][tmp]
        dp[i] = box
        # arr[0][i] = max(arr[0][i-1], arr[1][i-1]) + 1
        # arr[1][i] = max(arr[0][i-1], arr[1][i-1])
        arr[i] = arr[tmp] + 1

print(arr)

# arr[0] = 1
# for i, box in enumerate(boxes,1):
    
#     if boxes[i-1] < box:
#         arr[i] = arr[i-1] + 1
#     else:
#         tmp = i-1
#         while tmp>0:
#             tmp -= 1
#             if boxes[tmp] < box:
#                 break
#         arr[i] = arr[tmp] + 1

# print(arr)