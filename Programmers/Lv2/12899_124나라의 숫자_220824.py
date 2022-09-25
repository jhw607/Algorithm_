def solution(n):
    answer = ''
    # q,r = n,0
    # num = []
    while n:
        if n%3 == 0:
            answer = '4' + answer
            n = n//3 - 1
        else:
            answer = str(n%3) + answer
            n = n//3
    # print(num)
    # num = list(map(str, num))
    # num = ''.join(num)
    # print(num)
    # while num:
    #     tmp = num.pop()
    #     if tmp == '1':
    #         answer += '1'
    #     elif tmp == '2':
    #         answer += '2'
    #     else:
    #         answer += '4'
        
    return answer