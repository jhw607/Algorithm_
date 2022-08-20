def solution(s):
    answer = ''
    idx, r = divmod(len(s),2)
    if r == 0:
        answer = s[idx-1:idx+1]
    else:
        answer = s[idx]
        
    return answer

### 코드 줄이기
def solution(s):
    idx, r = divmod(len(s),2)
    return s[idx-1:idx+1] if r == 0 else s[idx]
        