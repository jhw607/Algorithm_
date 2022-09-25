from collections import deque

def solution(numbers, target):
    answer = 0
    # 각 값에 대한 더하는 경우, 빼는 경우를 다 큐에 넣음
    # 몇번째 계산인지는 필요하겠지
    # +,-니까 순서 상관없이 다 해보기만 하면 되는거
    # 그러니까 앞에서부터 2가지 경우 다 고려해주기만 하면 됨
    
    queue = deque()
    
    # 두 케이스는 각각의 인덱스로 계산횟수를 더해갈거
    queue.append([numbers[0], 0])
    queue.append([-1*(numbers[0]), 0])
    
    while queue:
        nums, idx = queue.popleft()
        idx += 1
        
        # 아직 덜 돌았다면
        if idx < len(numbers):
            queue.append([nums+numbers[idx], idx])
            queue.append([nums-numbers[idx], idx])
        else:
            if nums == target:
                answer += 1
            
            
    return answer



    