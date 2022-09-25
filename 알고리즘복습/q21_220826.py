# 인구 이동
# boj 16234

# 국경선을 공유하는 두 나라의 인구차이가 L명 이상 R명 이하라면
#     -> 두 나라가 공유하는 국경선을 열어줌
# 다 열리면 이동 시작
# 국경선이 열려있어 인접한 칸만 이용해 이동할 수 있으면
#     -> 두 나라는 연합
# 연합을 이루고 있는 각 칸의 인구수는
#     -> 연합 인구수 / 연합 칸수
#     -> 소수점은 버림
# 연합을 해체하고 국경선을 닫음

from collections import deque

def open_door(x,y,idx):
    # 연합에 속하는 국가들 좌표
    union = [] 
    union.append((x,y))
    graph[x][y] = idx
    queue = deque([(x,y)])
    union_sum = countries[x][y]
    union_cnt = 1
    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue
            if graph[nx][ny] == 0:                
                if l <= abs(countries[nx][ny] - countries[x][y]) <= r:
                    # 해당 국가가 어느 연합에 속하는지 저장
                    graph[nx][ny] = idx
                    # 연합 총 인구수에 더함
                    union_sum += countries[nx][ny]
                    # 연합 국가 수 +1
                    union_cnt += 1
                    # 연합 인구수 갱신을 위해 연합 국가에 추가
                    union.append((nx,ny))
                    # 이어서 탐색하기 위해 큐에 추가
                    queue.append((nx,ny))

    for ux,uy in union:
        countries[ux][uy] = union_sum//union_cnt
    return

n,l,r = map(int, input().split(' '))
countries = [list(map(int, input().split(' '))) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
total = 0

while True: 
    # while 한 턴이 하루

    # 어느 연합에 들어갔는지? 연합 index 저장
    graph = [[0]*n for _ in range(n)]

    idx = 1
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 0:
                open_door(i,j,idx)
                idx += 1
    
    if idx == n*n+1:
        break
    total += 1

print(total)