from heapq import heappush, heappop, heapify
from collections import deque
def solution(jobs):
    answer = 0
    n = len(jobs)
    # 요청부터 종료까지 걸린 시간의 평균의 최소
    # 1순위가 요청순서 2순위가 처리시간?
    jobs.sort(key = lambda x:x[0])
    jobs = deque(jobs)
    cur, start, total, cnt = 0, -1, 0, 0
    heap = []
    heap_order = []
    heap_process = []
    # for i, job in enumerate(jobs):
    #     heappush(heap, (job[1],job[0]))
    #     heappush(heap_order, (job[0],i))
    #     heappush(heap_process, (job[1],i))
    ready = []
    while cnt<n:
        ### print(ready)
        # while jobs and start<jobs[0][0]<=cur:
        #     o, p = jobs.popleft()
        #     heappush(ready, (p,o))
        for job in jobs:
            ### print('for', jobs)
            ### print(start, cur)
            if start < job[0] <= cur:
                heappush(ready, (job[1],job[0]))
                ### print('push', ready)
        if not ready:
            cur += 1
        #! while ready: 여기가 문제
        while ready:
            process, order = heappop(ready)
            start = cur
            total += cur+process-order
            cnt += 1
            cur += process
    answer = total // n
    
    #?### 정렬로는 안됨 #####
    # jobs.sort(key = lambda x:x[0])
    # jobs.sort(key = lambda x:x[1])
    # cur = 0
    # total = 0
    # print(jobs)
    # for order, process in jobs:
    #     if cur <= order:
    #         total += process
    #         cur = order + process
    #     elif cur > order:
    #         total += cur-order+process
    #         cur += process
    #     # else:
    #     #     total += process
    #     #     cur += process
    #     print(total, cur)
    # answer = total // len(jobs)
        
    return answer