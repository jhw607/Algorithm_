# n = int(input())
# sg = set(map(int, input().split(' ')))
# m = int(input())
# nums = list(map(int, input().split(' ')))
# answer = []

# for num in nums:
#     if num in sg:
#         answer.append(1)
#     else:
#         answer.append(0)


# print(*answer)


##################### 이분탐색 ######################

n = int(input())
sg = list(map(int, input().split(' ')))
m = int(input())
nums = list(map(int, input().split(' ')))
# answer = []
sg.sort()

for num in nums:
    left,right = 0, n-1
    while left<=right:
        mid = (left+right)//2
        if sg[mid]==num:
            print(1)
            break
        elif sg[mid]<num:
            left = mid+1
        else: 
            right = mid-1
    else:
        print(0)


# print(*answer)