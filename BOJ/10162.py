t = int(input())
times = [300, 60, 10]
answer = []

if t%10:
    answer.append(-1)
else:
    for time in times:
        q, t = divmod(t, time)
        answer.append(q)
    

print(*answer)