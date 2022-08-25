def solution(s):
    answer = len(s)
    for i in range(1, len(s)//2 + 1):
        cur = ''
        tmp = s[:i]
        cnt = 1
        for j in range(i, len(s), i):
            
            if tmp == s[j:j+i]:
                cnt += 1
            else:
                if cnt == 1:
                    cur += tmp
                else:
                    cur += str(cnt)+tmp
                cnt = 1 # cnt 초기화
                # tmp = s[cnt*i:cnt*i+i]  
                tmp = s[j:j+i]   # 여기서부터 다르다는 거니까 다시 시작하면 되겠네;;
        if cnt == 1:
            cur += tmp # 이걸로 다 flush가 됨?
        else:
            cur += str(cnt) + tmp
        
        answer = min(answer, len(cur))
        
        
    
    return answer