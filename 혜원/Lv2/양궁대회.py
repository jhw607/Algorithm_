from collections import deque
from copy import deepcopy
def solution(n, info):
    answer = [[], 0]
    apeach = 0
    ryan = 0
    
    # 점수
    queue = deque()
    new = [0]*11
    queue.append([[info[0]+1,0,0,0,0,0,0,0,0,0,0], 0])
    queue.append([[0,0,0,0,0,0,0,0,0,0,0], 0])
    
    while queue:
        scores, idx = queue.popleft()
        idx += 1
        if sum(scores) == n or idx == 11:
            for i, score in enumerate(scores):
                if score:
                    ryan += 10-i
                else:
                    apeach += 10-i if info[i] else 0
            if ryan>apeach:
                if answer[1] < ryan-apeach:
                    answer[0] = scores
                    answer[1] = ryan-apeach
                elif answer[1] == ryan-apeach:
                    
                    flag = False
                    for a, s in zip(answer[0], scores):
                        if a<s:
                            answer[0] = scores
                            
        else:
            tmp1 = deepcopy(scores)
            tmp2 = deepcopy(scores)
            queue.append([tmp1,idx])
            tmp2[idx] = info[idx]+1
            queue.append([tmp2,idx])
        
                        
    
    return answer