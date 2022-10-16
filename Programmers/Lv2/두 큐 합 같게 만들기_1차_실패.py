from collections import deque

def move(default,q1,q2,cnt):
    
    if sum(q1) == sum(q2):
        return cnt
    if (q1,q2) == default:
        return 0
    
    q2.append(q1.popleft())
    move(default,q1,q2,cnt+1)
    q1.appendleft(q2.pop())
    q1.append(q2.popleft())
    move(default,q1,q2,cnt+1)
    q2.appendleft(q1.pop())
    
    return res

def solution(queue1, queue2):
    
    q1 = deque(queue1)
    q2 = deque(queue2) 
    ring = deque(queue1+ [0] +queue2)
    answer = ring.index(0)
    # print(ring)
    p1,p2 = 0, 0
    q,r = divmod(sum(queue1) + sum(queue2),2)
    # print(q,r)
    # 반반이 불가능한 경우 : 홀수이거나 반보다 큰 값이 있거나
    if r or max(ring)>q:
        return -1
    
    while p2<=len(ring):
        tmp = sum(ring[i] for i in range(p1,p2))
        # print(p1,p2,tmp)
        if tmp < q:
            p2+=1
            # if p2 == len(ring): p2 = 0
        elif tmp > q:
            p1+=1
        else:
            break
    else:
        return -1
    
    # print(p1,answer,p2)
    # if p1<p2:
    if answer<p1:
        # return (p2-answer)+len(q1)
        return len(q1)+p2+p1-2*(answer+1)
    elif p1<=answer<=p2:
        return (p2-1-answer)+p1
    else:
        return p2+p1+len(q2)
#     else:
#         if answer<p2:
            
#         elif p2<answer<p1:
#         # return p1+p2+len(queue2)
#         return answer-p2
#         else:
#         return p2-answer
        
        
    # if (sum(q1)+sum(q2))%2 != 0:
    #     return -1
    # else:
    #     tmp = move((q1,q2),q1,q2,0)
    #     return tmp if tmp!=0 else -1
        