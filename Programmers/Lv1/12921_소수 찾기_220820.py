# def isPrime(num):
#     nums = [True for _ in range(num+1)] # 2,...,num
#     for i in range(2, num):
#         if nums[i]:
#             if num%i == 0:
#                 # print('nums:', nums)
#                 return False
#             else:
#                 tmp = num//i
#                 # print('tmp, num, i:', tmp, num, i)
#                 for j in range(tmp, 1, -1):
#                     # print('tmp, j, i:', tmp, j, i)
#                     nums[j*i] = False
#     else:
#         print('nums:', nums)
#         return True

# print(isPrime(int(input())))


def isPrime(num):
    nums = [True for _ in range(num+1)] # 2,...,num
    nums[0], nums[1] = False, False
    
    for i in range(2, num+1):
        if nums[i]:
            for j in range(i+i, num+1, i): 
                nums[j] = False
    # print(nums)
    return nums

def solution(n):
    return isPrime(n).count(True)



### 에라토스테네스의 체 : 범위 내 소수만 True로 남음