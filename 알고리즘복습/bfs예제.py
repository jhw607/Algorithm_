from collections import deque

n,m = map(int, input().split(' '))
maps = [input() for _ in range(n)]  # n줄 m칸
graphs = [[0]*m]*n  # n,m해당 위치까지의 이동횟수

dx = [-1, 1, 0, 0] # 상하좌우
dy = [0, 0, -1, 1] # 상하좌우

def bfs(x, y):

    queue = deque((x,y))    # 첫번째 탐색

    while queue:

        x, y = queue.popleft()  # 현재 위치

        for i in range(4):      # 현재 위치에서 상하좌우 탐색
            nx = x + dx[i]      # 다음 위치
            ny = y + dy[i]
            
            # 범위 밖이면 무시(다음 탐색)
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            # 0이면 -> 벽이니까 무시(다음 탐색)
            if maps[nx][ny] == 0:
                continue
            # 1이면 -> 처음 방문 -> 현재횟수 + 1 , 큐에 추가
            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y]+1
                queue.append((nx,ny))

    # 우측 최하단(최종목적지) : 총 이동 횟수
    return maps[n-1][m-1]

print(bfs(0,0))