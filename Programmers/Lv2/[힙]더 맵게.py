from heapq import heappush, heappop, heapify
def solution(scoville, K):
    answer = 0
    min_k = min(scoville)
    heapify(scoville)
    while scoville[0]<K:
        if len(scoville)<2:
            return -1
        a = heappop(scoville)
        b = heappop(scoville)
        c = a + b*2
        heappush(scoville,c)
        answer += 1
    return answer