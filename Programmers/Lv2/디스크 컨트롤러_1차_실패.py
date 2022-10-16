import heapq
from heapq import heappush, heappop

def solution(jobs):
    hq = []
    answer = 0
    
    # for job in jobs:
    #     job += [0,0]
        # heapq.heappush(hq, job)
    jobs_s = sorted(jobs, key = lambda x : x[1])
    jobs_r = sorted(jobs, key = lambda x : x[0])
    jobs.sort(key = lambda x : x[9])
    
    # 가장 낮은 기준이 선착순
    # 들어온 시점에 시간 제일 짧은 거부터?
    # ntt 계산해서?
    # 실행시간 대비 기다린시간?
    # jobs = [s요청시점, r실행시간, w대기시간, e반환시간]
    # 시간이 흐른다치고 
    i = 0
    process = 0
    
    while True:
        # 대기+실행 보다 현재-대기 작으면 계속
        if i-jobs_t[process][2] < jobs_t[pocess][2]+jobs_t[process][1]:
            # continue
        else: # 프로세스 하나 끝남
            jobs_t.remove(jobs[process])
            jobs_s.remove(jobs[process])
            # 다음 프로세스 결정
            min_idx = 0
            min = 1001
            for i, job in enumerate(jobs):
                job[0] += i
                if min>job[1]: 
                    min = job[1]
                    min_idx = i
            process = min_idx
            
        for t,s = zip(jobs_t, jobs_s):
            t[2] += 1
            s[2] += 1
        
        i+=1
        
    print(jobs)
    return answer