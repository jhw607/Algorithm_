from collections import Counter
def solution(N, stages):
    answer = []
    stage_dic = Counter(stages) # stage : 사용자수
    fail = []   # 스테이지별 실패율
    for stage in range(1, N+2):
        fail.append([stage_dic[stage], stage])  # [사용자수, stage]
    fail.sort(key = lambda x:x[1])  
    users = 0   # 스테이지에 도달한 플레이어 수
    for stage in range(N+1, 0, -1):
        users += fail[stage-1][0]
        if users == 0:
            fail[stage-1][0] = 0
        else:
            fail[stage-1][0] /= users
    fail.sort(key = lambda x:-x[0])
    answer = [x[1] for x in fail if x[1]<=N]
    print(fail)
    return answer