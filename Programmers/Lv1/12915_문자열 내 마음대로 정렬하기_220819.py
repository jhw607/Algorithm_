def solution(strings, n):
    answer = []
    temp = []
    for str in strings:
        temp.append((str[n], str))
    temp.sort()
    answer = list(t[1] for t in temp)
    return answer