def solution(s):
    answer = True
    p_cnt = s.count('p')+s.count('P')
    y_cnt = s.count('y')+s.count('Y')
    if p_cnt != y_cnt:
        return False
    return True