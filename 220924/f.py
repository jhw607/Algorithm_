from collections import deque

def move(n, m, x, y, record, visited, k, ans, results):

    dirct = ['u','d','l','r']
    if len(record)==k:
        if (x,y) == ans:
            results.append(''.join(record))    
        return 
    que = deque((x,y))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while que:
        cx,cy = que.popleft()
        for i in range(4):
            nx = cx+dx[i]
            ny = cy+dy[i]

            if 0<nx<n and 0<ny<m:
                visited[nx][ny] = visited[cx][cy]+1
                record.append(dirct[i])
                move(n, m, nx, ny, k, ans, record, visited, results)
                record.pop()
                visited[nx][ny] = 0


    
def solution(n, m, x, y, r, c, k):
    answer = ''
    que = deque((x,y))
    results = []
    record = []
    visited = [[0]*m]*n
    move(n, m, x, y, record, visited, k, (r,c), results)
                
        
    print(results)
    return answer

solution(3,4,2,3,3,1,5)