# 연구소
# b0j 14502

from collections import deque
from copy import deepcopy

def virus():

    maps = deepcopy(graph)
    queue = deque()
                
    for row in range(len(maps)):
        for col in range(len(maps[0])):
            if maps[row][col] == 2:
                queue.append((row,col))

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx<0 or ny<0 or nx>=len(maps) or ny>=len(maps[0]):
                continue
            if maps[nx][ny] == 0:
                maps[nx][ny] = 2
                queue.append((nx,ny))
    # print(maps)
    safe(maps)
    return 

def wall(count,n,m):

    if count == 3:
        virus()
        return
    # print('wall', count)
    for a in range(n):
        for b in range(m):
            # print(a,b,count)
            if graph[a][b] == 0:
                graph[a][b] = 1
                wall(count+1,n,m)
                graph[a][b] = 0
                

def safe(maps):
    global answer
    cnt = 0
    for row in maps:
        cnt += row.count(0)
    answer = max(cnt, answer)
    return

n, m = map(int, input().split(' '))
graph = [list(map(int, input().split(' '))) for _ in range(n)]
answer = 0
# print(graph)

dx = [-1,1,0,0]     # 상,하,좌,우
dy = [0,0,-1,1]     # 상,하,좌,우


wall(0,n,m)

print(answer)

