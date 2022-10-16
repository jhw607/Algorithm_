from collections import deque
def solution(queue1, queue2):
    answer = 0
    q1, q2 = deque(queue1), deque(queue2)
    total = sum(q1) + sum(q2)
    half, r = divmod(total,2)
    tmp = sum(q1)
    if r or half < max(max(q1),max(q2)):
        return -1
    while tmp != half:
        # 3
        gap = abs(tmp-half)
        p_sum = 0
        if tmp>half:
            # p_sum = q1[0]
            # # 2
            # for i in range(1, len(q1)):
            #     if p_sum+q1[i] <= gap:
            #         p_sum += q1[i]
            #     else:
            #         # ttmp = [q1.popleft() for _ in range(i)]      
            #         # q2.extend(ttmp)
            #         for _ in range(i):
            #             a = q1.popleft()
            #             q2.append(a)
            #             # tmp -= a                    
            #             answer += 1
            #         break
            # tmp -= p_sum
            # 1
            tmp -= q1[0]
            q2.append(q1.popleft())
        else:
            # p_sum = q2[0]
            # for i in range(1, len(q2)):
            #     if p_sum+q2[i] <= gap:
            #         p_sum += q1[i]
            #     else:
            #         # ttmp = [q2.popleft() for _ in range(i)]      
            #         # q1.extend(ttmp)
            #         for _ in range(i):
            #             a = q2.popleft()
            #             q1.append(a)
            #             # tmp -= a
            #             answer += 1
            #         break
            # tmp += p_sum
            tmp += q2[0]
            q1.append(q2.popleft())
        answer += 1
        # tmp = sum(q1)
        # tmp += -p_sum if tmp>half else p_sum
        # print(tmp, q1, q2)
        # if q1 == queue1:
        #     answer = -1
        #     break
    return answer