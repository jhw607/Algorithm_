def func(n, total, cnt):
    if cnt == 0:
        print('total',total)
        return total
    visited[n] = True
    for c, v in graph[n]:
        if visited[v] == False:
            print(n, v, c, total, cnt)
            return func(v, total+c, cnt-1)            


n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b,cost = map(int, input().split(' '))
    graph[a].append((cost,b))
    graph[b].append((cost,a))
# print(graph)
graph = list(map(sorted, graph))
# print(graph)

visited = [False]*(n+1)
answer = func(1, 0, n-1)
print(answer)
   