from collections import defaultdict
def solution(records):
    answer = []
    # 아이디별 마지막 닉네임이랑 in/out메시지 인덱스 저장
    members = defaultdict()
    msg = []
    idx = 0
    for r in records:
        # print(r.split(' '))
        record = r.split(' ')
        word = record[0]
        uid = record[1]
        if word == 'Leave':
            msg.append([word, uid])    
        else:
            nickname = record[2]
            
            # >>> 이게 더 빠름..; <<<
            if word == 'Change':
                members[uid] = nickname                
            else:
                msg.append([word, uid])                
                members[uid] = nickname

            # >>> 이거보다 <<<
            # if word == 'Enter':
            #     msg.append([word, uid])                
            # members[uid] = nickname
                
    for word, uid in msg:
        if word == 'Enter':
            tmp = members[uid]+'님이 들어왔습니다.'
        else:
            tmp = members[uid]+'님이 나갔습니다.'
        answer.append(tmp)
        
    return answer