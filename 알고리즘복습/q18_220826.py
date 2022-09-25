# 괄호 변환
# 프로그래머스 60058

def check(s):
    s = list(s)
    stk = []
    if s[-1] == '(':
        return False
    else:
        stk.append(s.pop()) # ')'
        while s:
            tmp = s.pop()
            if tmp == '(':
                if stk: stk.pop()
                else: return False
            else:
                stk.append(tmp)
        if stk:
            return False
        else:
            return True
        
def func(s):

    if s == '':
        return ''
    if check(s):
        return s

    cnt = 0
    u, v = '',''
    for idx, i in enumerate(s):
        print('for', idx, i, u, v, cnt)
        if i=='(':
            cnt += 1
        else:
            cnt -= 1
        if cnt == 0:
            u = s[:idx+1]
            v = s[idx+1:]
            break

    if check(u):
        return u + func(v)
    else:
        print('u',u,'v',v)
        return '('+ func(v) +')' + reverse_u(u[1:-1])

def reverse_u(s):
    print('reverse s:',s)
    result = []
    for i in s:
        if i=='(':
            result.append(')')
        else:
            result.append('(')
    result = ''.join(result)
    print('reverse result:', result)
    return result


def solution(p):
    answer = ''
    
    # '(',')' 개수가 같음 : 균형잡힌 괄호 문자열
    # 짝도 맞음 : 올바른 괄호 문자열
    
    # 1. 빈문자열 -> 빈문자열
    # 2. w를 더이상 분리할 수 없는 균형잡힌 문자열 u와 v(빈문자열가능)로 분리
    # 3. u가 올바른 괄호 문자열 -> v가지고 1단계부터
        # -> 수행한 결과를 u에 이어붙이고 반환
    # 4. u가 올바른 괄호 문자열이 아닐때
        # -> '(' + v를 1단계부터 수행한 결과 + ')' 에다가
        # -> u의 첫번째와 마지막 문자 제거하고 괄호 뒤집은 걸 붙임
            
    answer = func(p)
        
    return answer