from heapq import heappush, heappop, heapify
def solution(operations):
    answer = []
    nums = []
    min_heap = []
    max_heap = []
    for operation in operations:
        oper, num = operation.split(' ')
        num = int(num)
        if oper == 'I':
            heappush(min_heap,num)
            heappush(max_heap,num*-1)
        else:
            if min_heap:
                if num < 0:
                    heappop(min_heap)
                    max_heap = [i*-1 for i in min_heap]
                    heapify(max_heap)
                else:
                    heappop(max_heap)
                    min_heap = [i*-1 for i in max_heap]
                    heapify(min_heap)
    if min_heap:
        answer = [max_heap[0]*-1, min_heap[0]]
    else:
        answer = [0, 0]
            
    return answer