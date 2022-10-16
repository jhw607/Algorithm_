from collections import deque
def solution(queue1, queue2):
    answer = 0
    q1, q2 = deque(queue1), deque(queue2)
    total = sum(q1) + sum(q2)
    half, r = divmod(total,2)
    tmp = sum(q1)
    if r or half < max(max(q1),max(q2)):
        return -1
    for _ in range(len(queue1)*3):
        if tmp > half:
            tmp -= q1[0]
            answer+=1
            q2.append(q1.popleft())
        elif tmp < half:
            tmp += q2[0]
            answer+=1
            q1.append(q2.popleft())
        else:
            break
    else:
        answer = -1
    return answer