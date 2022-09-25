# (r,c)

# 현재위치 청소
# 왼: 빈공간 -> 좌회전 1전진 청소
#   : 아니면 -> 좌회전
# 왼쪽한칸 못가는걸(왼쪽회전만하는걸) 4번하면
# -> 후진(벽이면 중지)

# 방향 d : 0,1,2,3 : 위,오른,아래,왼

# 빈칸 0, 벽 1

# 청소 : 카운트(visited)
# 이동 : 왼쪽 확인 및 전진 d갱신(-1)

def check(robo):     # 왼쪽이 벽인지
    r,c,d = robo
    # 0,1,2,3 : 위 오 아 왼
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    
    idx = (d-1)%4   # 현위치 r,c의 왼쪽한칸
    # print("check : ", floor[r+dr[idx]][c+dc[idx]])
    return not floor[r+dr[idx]][c+dc[idx]] and not answer[r+dr[idx]][c+dc[idx]]

def move(robo):       # 왼쪽한칸으로 이동
    r,c,d = robo
    # 0,1,2,3 : 위 오 아 왼
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    
    idx = (d-1)%4   # 현위치 r,c의 왼쪽한칸
    robo = [r+dr[idx], c+dc[idx], d-1]
    answer[r+dr[idx]][c+dc[idx]] = 1
    return robo

def isBack(robo):  # 후진
    r,c,d = robo
    # 0,1,2,3 : 위 오 아 왼
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    
    idx = (d-2)%4   # 현위치 r,c의 뒷칸
    return not floor[r+dr[idx]][c+dc[idx]]

def goBack(robo):  # 후진
    r,c,d = robo
    # 0,1,2,3 : 위 오 아 왼
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    
    idx = (d-2)%4   # 현위치 r,c의 뒷칸
    robo = [r+dr[idx], c+dc[idx], d]    # 후진
    return robo



n,m = map(int, input().split(' '))
r,c,d = map(int, input().split(' '))
floor = []
robo = [r,c,d]
answer = []

for _ in range(n):
    floor.append(list(map(int, input().split(' '))))
    answer.append([0]*n)
isStop = 0
answer[r][c] = 1
while isStop<4:
    # print(robo)
    # print("answer: \n", answer)
    if check(robo):
        # print("move")
        robo = move(robo)
        isStop = 0
    else:
        # print("rotate")
        robo[2] -= 1
        isStop += 1
    if isStop == 4:
        # print("4")
        if isBack(robo):
            # print("goBack")
            robo = goBack(robo)
            isStop = 0
        else:
            break
        
# print(answer)
s=0
for ans in answer:
    s += sum(ans)
print(s)