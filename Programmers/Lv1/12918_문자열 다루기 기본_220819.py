def solution(s):
    n = len(s)
    if (n==4 or n==6) and s.isdigit(): return True
    else: return False