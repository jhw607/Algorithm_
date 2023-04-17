# sol1
def solution(babbling):
    answer = 0
    words = ['aya','ye','woo','ma']
    for babb in babbling:
        if babb[0] not in ['a', 'y', 'w', 'm']:
            continue
        while babb:
            for word in words:
                if babb[:len(word)] == word:
                    babb = babb[len(word):]
                    break;
            else:
                if babb:
                    break
        if not babb: answer+=1
    return answer


# sol2
def solution(babbling):
    words = ['aya','ye','woo','ma']
    answer = 0
    for babb in babbling:
        temp = babb
        for word in words:
            temp = temp.replace(word, ' ')
        if len(temp.replace(' ','')) == 0:
            answer += 1
    return answer
