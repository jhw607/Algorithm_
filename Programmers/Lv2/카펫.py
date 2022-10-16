def solution(brown, yellow):
    answer = []
    # 노란색 모양을 정하고
    #   가로 > 세로 1:1, 2:1, 2:2, 3:1, 3:2, 3:3 이런식?
    # 갈색 개수가 맞는지 확인
    # 곱해서 yellow가 나오는 자연수 조합 -> 약수 구하기
    nums = []
    for i in range(1, yellow+1):
        q,r = divmod(yellow, i)
        # if i > q: break
        if r == 0:
            if (q+i)*2+4 == brown:
                answer = [q+2,i+2]
                break
            
    return answer
# 20분