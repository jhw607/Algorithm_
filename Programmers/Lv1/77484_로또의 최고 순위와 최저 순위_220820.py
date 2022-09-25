def solution(lottos, win_nums):
    answer = []
    cnt, z_cnt = 0, 0
    for lotto in lottos:
        if lotto > 0:
            if lotto in win_nums: cnt +=1
        else:
            z_cnt+=1
    cnt = 1 if cnt==0 else cnt
    z_cnt = 5 if z_cnt==6 else z_cnt
    answer = [7-cnt-z_cnt, 7-cnt]
    return answer

# cnt, z_cnt 예외처리 더 깔끔하게 할 수 있을텐데;
