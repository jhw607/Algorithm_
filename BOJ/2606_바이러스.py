def func(n, visited):
    print(n)
    visited[n] = True
    for i in graph[n]:
        if not visited[i]:
            func(i, visited)


coms = int(input())
n = int(input())
graph = [[] for i in range(coms+1)]
visited = [False]*(coms+1)
for _ in range(n):
    a,b = map(int, input().split(' '))
    graph[a].append(b)
    graph[b].append(a)

print(graph)
func(1, visited)
print(visited)
cnt=0
for v in visited:
    if v:
        cnt += 1
print(cnt-1)
