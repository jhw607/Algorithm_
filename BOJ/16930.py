n, m, k = map(int, input().split(' '))
dom = [input() for _ in range(n)]
x1, y1, x2, y2 = map(int, input().split(' '))
visited = [[0]*m for _ in range(n)]
start = (x1-1, y1-1)
end = (x2-1, y2-1)
# print(n,m,k)
# print(dom)
# print(visited)
# print(start, end)

w = k
dx = [-1, 1, 0, 0] # 위,아래,오른쪽,왼쪽
dy = [0, 0, 1, -1]
x,y = start
sec = 0
while (x,y) != end:
    for i in range(4):
        cnt = 0
        sec += 1
        while dom[x][y] == '.':
            print(x,y)
            cnt += 1
            x += dx[i]
            y += dy[i]
            if cnt==k:
                break
    if (x,y) == start:
        print(-1)

print(sec)

if 0 <= x < n and 0 <= y < m:
    if visited[x][y]==False:
        for i in range(4):
            cnt = 0
            while cnt < k:
                if dom[x][y]=='#':
                    break
                cnt += 1
                x += dx[i]
                y += dy[i]
            func(n, m, x, y)