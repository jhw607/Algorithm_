def solution(s):
# >>> sol2 <<<
    answer = True
    stk = []
    if s[-1]=='(' or s[0]==')':
        answer = False
    else:
        for i in s:
            if i=='(': stk.append('(')
            else: 
                if stk: stk.pop()
                else: answer = False; break;
        else:
            if stk:
                answer = False
                
# >>> sol1 <<<
    # answer = False
    # stk = []
    # s = list(s)
    # if s[-1]=='(' or s[0]==')':
    #     return answer
    # else:
    #     while s:
    #         if s[-1] == ')':
    #             stk.append(s.pop())
    #         else:
    #             s.pop()
    #             if stk: stk.pop()
    #             else: return answer
    #     if stk: return answer
    #     answer = True
                
    return answer