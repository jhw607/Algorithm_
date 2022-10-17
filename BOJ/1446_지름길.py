# 지름길
# n: 지름길 개수 <= 12
# d: 고속도로 길이 <= 10,000
# 위치 : 노드
# 지름길 : 간선
# 시작위치 < 도착위치 
#? 아 고속도로 총길이 상의 위치구나
#? 그럼 지름길은 점프냐; 구불구불하다니까뭐..(길어지기도 하더만;)

from heapq import heappush, heappop, heapify
n, d = map(int, input().split(' '))

# graph = [[] for _ in range(10001)] # 이럴 필요 없이
graph = [[] for _ in range(d+1)]     # 조건으로 걸러주면 됨
for _ in range(n):
    start, end, cost = map(int, input().split(' '))
    # heappush(graph[start],(cost, end))
    if start>d or end>d: continue
    graph[start].append((cost,end))

dist = [i for i in range(10001)]
for i in range(d):
    for cost, next in graph[i]:
        dist[next] = min(dist[i]+cost,dist[next])
    # 2 - 훨씬 근본적인 답
    dist[i+1] = min(dist[i]+1, dist[i+1])
    # 1 - 왜케 꼬아서 생각했을까;
    # for j in range(i, d+1):
    #     dist[j] = min(dist[i]+(j-i), dist[j])

    # 힙은 필요없었다..ㅎ
    # cost, next = heappop(graph[i])

# print(dist[:d+1])
print(dist[d]) # answer
    