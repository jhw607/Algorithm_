def solution(a, b):
    answer = 0
    if a==b:
        answer = a
    else:
        term = 1 if a<b else -1
        for i in range(a, b+term, term): answer += i
    return answer

### a,b 대소관계를 일정하게
def solution(a, b):
    answer = 0
    if a>b : a,b = b,a # 무조건 a<b 이도록
    for i in range(a,b+1):
        answer += i
    return answer