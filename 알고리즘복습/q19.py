# 연산자 끼워 넣기
# boj 14888

from itertools import permutations

def calc(a,b,op):
    if op == '+':
        return a+b
    elif op == '-':
        return a-b
    elif op == '*':
        return a*b
    else:
        if a<0: return -1*(abs(a)//b)
        else: return a//b

n = int(input())
nums = list(map(int, input().split(' ')))
opers = list(map(int, input().split(' ')))

ops = '+'*opers[0] + '-'*opers[1] + '*'*opers[2] + '/'*opers[3]
# print(ops)
ops = list(ops)
# print(ops)

# cases = permutations(ops,n-1)




