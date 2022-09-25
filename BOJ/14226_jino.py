import sys
from collections import deque

input = sys.stdin.readline

num = int(input())

q = deque([[1, 0, 0]])

answer = set()

while q:

    monitor, clipboard, time = q.popleft()

    if monitor == num:
        print(time)
        break

    if (monitor, clipboard) in answer:
        continue
    else:
        answer.add((monitor, clipboard))

    for i in range(3):

        if i == 0:
            q.append((monitor, monitor, time + 1))
        elif i == 1 and clipboard:
            q.append((monitor+clipboard, clipboard, time+1))
        elif i == 2 and monitor-1 > 0:
            q.append((monitor-1, clipboard, time+1))