# 특정 거리의 도시 찾기
# 18352

from collections import deque, defaultdict
from operator import ne

# 1~n개의 도시, m개의 단방향 도로, 모든 도로는 거리 1
# 최단거리가 k인 도시들을 출력

# 최단거리를 구하고 k인지 확인

n, m, k, x = map(int, input().split(' '))
graph = defaultdict(list)
cities = []

# x에서 출발해 해당 도시까지 가는 거리
visited = [-1]*(n+1)        

for _ in range(m):
    a,b = map(int, input().split(' '))
    # 단방향, a에서 b로만 갈 수 있음
    graph[a].append(b)      

queue = deque([x])
# x에서 x까지 가는 거리는 0
visited[x] = 0              

while queue:

    # 현재 도시
    city = queue.popleft()      

    # 다리로 연결된 다음 도시
    for next in graph[city]:     

        # 첫 방문 -> 현재도시까지 이동횟수 + 1 , 큐에 추가
        if visited[next] == -1:         
            visited[next] = visited[city] + 1
            queue.append(next)

for i in range(1, n+1):                 
    # 이동 거리가 k인 도시들만 추출
    if visited[i] == k:
        cities.append(i)

if cities: [print(c, end='\n') for c in cities]
else: print(-1)