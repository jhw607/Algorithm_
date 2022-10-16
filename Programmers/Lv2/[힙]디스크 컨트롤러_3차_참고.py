from heapq import heappush, heappop, heapify
from collections import deque
def solution(jobs):
    n = len(jobs)
    
    jobs.sort(key = lambda x:x[0])
    jobs = deque(jobs)
    cur, start, total, cnt = 0, -1, 0, 0
    ready = []
    while cnt<n:
        ### print(ready)
        # ready에 추가하기 1
        # while jobs and start<jobs[0][0]<=cur:
        #     o, p = jobs.popleft()
        #     heappush(ready, (p,o))
        # ready에 추가하기 2
        for job in jobs:
            if start < job[0] <= cur:
                heappush(ready, (job[1],job[0]))
        if not ready:
            cur += 1
        else:
            process, order = heappop(ready)
            start = cur
            total += cur+process-order
            cnt += 1
            cur += process
        
    return total // n