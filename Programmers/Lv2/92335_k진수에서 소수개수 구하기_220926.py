# https://school.programmers.co.kr/learn/courses/30/lessons/92335

from collections import deque
from math import sqrt

def isPrime(n):
    if n<2:
        return False
    for i in range(2,round(sqrt(n))+1):     # 이게 더 짧음
    # for i in range(2,round(n**(1/2))+1):  # 이거보다
        if n%i == 0:
            return False
    else:
        return True    
        
def transNum(n,k,result):
    if n == 0:
        return ''.join(list(map(str,result)))
    
    q,r = divmod(n,k)
    result.appendleft(r)
    return transNum(q,k,result)

def solution(n, k):
    result = deque()
    cnt = []
    
    if n==1: return 0
    print(dir(n))
    nums = transNum(n,k,result).split('0') if k<10 else str(n).split('0')
    # print(nums)
    for num in nums:
        if num: cnt.append(isPrime(int(num)))
    # print('cnt', cnt)
          
    return cnt.count(True)