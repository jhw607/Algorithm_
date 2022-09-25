def solution(s):
    answer = []
    arr = []
    sets = s[2:-2].split('},{')
    for elem in sets:
        elem = list(map(int, elem.split(',')))
        arr.append(elem)
    arr.sort(key = lambda x:len(x))
    answer.append(arr[0][0])
    for i in range(len(arr)-1):
        a,b =set(arr[i+1]), set(arr[i])
        c = list(a-b)[0]
        answer.append(c)    
    
    return answer