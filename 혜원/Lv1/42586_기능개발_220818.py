def solution(progresses, speeds):
# >>> sol2 <<<
    answer = []
    complete, cnt = 0,0
    for p,s in zip(progresses, speeds):
        q,r = divmod(100-p, s)
        days = q+1 if r > 0 else q
        if complete == 0:       #처음
            complete = days
            # cnt += 1
            answer.append(1)
        else:
            if complete < days:     # 이날 부터 다음 이날까지 배포
                answer[-1] += cnt
                cnt = 0
                complete = days
                answer.append(1)
            else:
                cnt += 1
    answer[-1] += cnt
    
    return answer
    
    
    
# >>> sol1 <<<
#     answer = []
#     complete, cnt = 0, 0 #완료일, 기능수
#     for p, s in zip(progresses, speeds):
#         q,r = divmod(100-p, s)
#         days = q+1 if r>0 else q
#         if complete<days: 
#             if complete!=0:
#                 answer.append(cnt+1)
#                 cnt = 0
#             complete = days
#         else: #배포
#             cnt += 1
#     answer.append(cnt+1)
    
#     return answer