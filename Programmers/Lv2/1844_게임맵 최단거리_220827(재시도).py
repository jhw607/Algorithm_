# >>> 리팩토링 <<<
from collections import deque

def solution(maps):
    answer = 0
    n, m = len(maps), len(maps[0])
    graph = [[0]*m for _ in range(n)]
    maps[0][0] = 1
    queue = deque([(0,0)])
    # 상하좌우
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if 0<=nx<n and 0<=ny<m:
                if maps[nx][ny] == 1:
                    maps[nx][ny] += maps[x][y]
                    queue.append((nx,ny))
    
    if maps[n-1][m-1]>1:
        answer = maps[n-1][m-1]
    else:
        answer = -1
    return answer



# >>> 재도전 <<< 

# def solution(maps):
#     answer = 0
#     n, m = len(maps), len(maps[0])
#     graph = [[0]*m for _ in range(n)]
#     graph[0][0] = 1
#     queue = deque([(0,0)])
#     # 상하좌우
#     dx = [-1,1,0,0]
#     dy = [0,0,-1,1]    
    
#     while queue:
#         x, y = queue.popleft()
        
#         for i in range(4):
#             nx = x+dx[i]
#             ny = y+dy[i]
            
#             if 0<=nx<n and 0<=ny<m:
#                 if maps[nx][ny] == 1:
#                     #? graph[nx][ny] = min(graph[x][y] + 1, graph[nx][ny])
#                     #? bfs는 어차피 가까운 곳부터 도니까 먼저 와서 입력되는 값이 최소일 거
#                     #? 따라서 비교할 필요없고 이동할 수 있는 칸의 default가 1이니까 더하면서 진행하면 됨
#                     queue.append((nx,ny))
    
#     if graph[n-1][m-1]:
#         answer = graph[n-1][m-1]
#     else:
#         answer = -1
#     return answer































# >>> 첫 시도 <<<

def func(dx, dy, cnt=0):
    if dx==n-1 and dy==m-1: return cnt 
    if dx==n or dy==m: return -1
    if cnt > n*m: return -1
    
    if map[dx+1][dy] == 1:
        return func(dx+1, dy, cnt+1)
    if map[dx][dy+1] == 1:
        return func(dx, dy+1, cnt+1)
    return -1

def solution(maps):
    answer = 0
    global n,m
    n,m = len(maps)-1, len(maps[0])-1
    print(func(0,0))
    
    return answer