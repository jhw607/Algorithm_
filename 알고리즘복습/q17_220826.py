# 경쟁적 전염
# boj 18405

from collections import deque

n, k = map(int, input().split(' '))
graph = [list(map(int, input().split(' '))) for _ in range(n)]
S, X, Y = map(int, input().split(' '))

# print(graph)

dx = [-1,1,0,0]
dy = [0,0,-1,1]

queue = list()
virus = []

for i in range(n):
    for j in range(n):
        v = graph[i][j]
        if v > 0:
            queue.append((v,0,i,j))

queue.sort()
queue = deque(queue)

while queue:    # 종료: 주어진 시간만큼 움직였거나, 모든 시험관이 감염되어 큐가 비었거나

    v,s,x,y = queue.popleft()

    if s==S:
        break

    for j in range(4):
        nx = x+dx[j]
        ny = y+dy[j]

        if nx<0 or ny<0 or nx>=n or ny>=n:
            continue
        if graph[nx][ny] == 0:
            graph[nx][ny] = v
            queue.append((v,s+1,nx,ny))
            # print(queue)

print(graph[X-1][Y-1])

