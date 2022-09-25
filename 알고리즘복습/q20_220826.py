# 감시 피하기
# boj 18428

from collections import deque
from itertools import starmap

# 장애물 3개 놓기
    # 선생님이 감시
    #     t를 큐에 넣고
    #     큐에서 꺼낸 위치에서
    #     상하좌우로 장애물 혹은 벽까지
    #// 학생으로 검사
    #//     s를 큐에넣고(좌표로)
    #//     큐에서 꺼낸 위치에서 
    #//     상하좌우로 t있는지
    #//     끝까지 없으면 YES
    #//     중간에 하나라도 나오면 NO

# 지금 graph를 기준으로 선생님눈에 걸리는 학생이 있는지
def check():
    # print(graph)
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    # 선생님 위치를 queue라는 리스트에 미리 넣어놓고 
    # check마다 deque 만들어서 사용
    teachers = deque(queue)
    # 주어진 방향으로 끝(벽 or 장애물)까지 가기 위한 큐
    straight = deque()

    
    while teachers:
        x,y = teachers.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or ny<0 or nx>=len(graph) or ny>=len(graph):
                continue
            if graph[nx][ny] == 'S':    # 학생 만나면 
                return False            # 바로 반환
            elif graph[nx][ny] == 'O':  # 장애물 만나면
                continue                # 탐색 멈춤
            else:                       # 계속 탐색
                straight.append((i, nx, ny)) 
            
            # 직진탐색 할 곳이 있는 동안 반복
            while straight: 
                dir, s_x, s_y = straight.popleft()
                
                s_nx = s_x+dx[dir]
                s_ny = s_y+dy[dir]
                if s_nx<0 or s_ny<0 or s_nx>=len(graph) or s_ny>=len(graph):
                    continue
                if graph[s_nx][s_ny] == 'S':
                    return False
                elif graph[s_nx][s_ny] == 'O':
                    break
                else:
                    straight.append((i, s_nx, s_ny))
    return True

def wall(count):

    # 3개 되면 check 호출, return을 answer에 저장
    if count == 3:
        answer.append(check())
        return

    # 벽 3개 세우는 모든 케이스
    for i in range(len(graph)):
        for j in range(len(graph)):
            if graph[i][j] == 'X':
                graph[i][j] = 'O'
                wall(count+1)
                graph[i][j] = 'X'



n = int(input())
graph = [input().split(' ') for _ in range(n)]

queue = []
# 하나라도 true가 있는지 판단하려고 return을 여기에 모음
answer = []
for i in range(len(graph)):
        for j in range(len(graph)):
            if graph[i][j] == 'T':
                queue.append((i,j))
           
wall(0)
if True in answer:
    print('YES')
else:
    print('NO')