def roll(key,dice):
    newDice = []
    idx = {1:[4,2,1,6,5,3], 2:[3,2,6,1,5,4], 3:[5,1,3,4,6,2], 4:[2,6,3,4,1,5]}
    
    for i in range(6):
        # newDice[i] = dice[idx[key]-1]
        newDice.append(dice[idx[key][i]-1])
    dice = newDice
    print(dice)
    return dice[0], dice[5]

# 밑으로 r, 오른쪽으로 c, 0부터
# 칸 0 : 주사위 바닥(그대로) -> 칸
# 아니면: 칸(0) -> 주사위 바닥
# 좌표와 명령을 수행한 주사위 상단의 값
# 밖으로 나가면 무시

n, m, x, y, k = map(int, input().split(' '))
maps = [list(map(int, input().split(' '))) for _ in range(n)]
instructions = list(map(int, input().split(' ')))   # 1,2,3,4 : 오, 왼, 위, 아래

# dice = [2,3,4,5,6,7]        # 위, 앞, 오, 왼, 뒤, 아 : 123456
dice = [0,0,0,0,0,0]        # 위, 앞, 오, 왼, 뒤, 아 : 123456
                            # 앞, 왼, 위, 뒤, 오, 아 : 123456




# key = 'right'
# roll(key)
pos = [x,y]
dx = [0,0,-1,1]
dy = [1,-1,0,0]

for instruction in instructions:
    x, y = x+dx[instruction-1], y+dy[instruction-1]
    top, bottom = roll(instruction,dice)
    if 0<=x<n and 0<=y<m:
        if maps[x][y] == 0:
            maps[x][y] = bottom
        else:
            dice[5] = maps[x][y]
            maps[x][y] = 0

print(dice[0])



# 오른쪽으로 구르면
# 0,2,0,0,5,0
# idx = [4,2,1,6,5,3]
# 5,3,2,7,6,4    
# # 1,6,2,4,3,5
# newDice = [0]*6
# for i in range(6):
#     newDice[i] = dice[idx-1] 

# 왼쪽으로 구르면
# 0,2,0,0,5,0
# idx = [3,2,6,1,5,4]
# # 1,3,5,4,6,2
# for i in range(6):
#     newDice[i] = dice[idx-1] 

# 앞으로 구르면
# 0,0,3,4,0,0
# 5,1,3,4,6,2
# for i in range(6):
#     newDice[i] = dice[idx-1] 

# 뒤로 구르면
# 0,0,3,4,0,0
# 2,6,3,4,1,5
# for i in range(6):
#     newDice[i] = dice[idx-1] ()