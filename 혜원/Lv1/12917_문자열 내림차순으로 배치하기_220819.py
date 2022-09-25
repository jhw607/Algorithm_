def solution(s):
    answer = ''.join(sorted(list(s), reverse=True))
    return answer

### 코드 줄이기
def solution(s):
    return ''.join(sorted(list(s), reverse=True))    