from queue import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    onBridge = [0]*bridge_length
    trucks = deque(truck_weights)
    # print(dir(trucks))
    # help(trucks.maxlen)
    n = len(trucks)
    if n == 1:
        answer = bridge_length+1
    else:
        while onBridge:
            answer += 1
            onBridge.pop(0)
            if trucks :
                if sum(onBridge)+trucks[0]<=weight:     # 한대 올라가도 무게가 견딜 수 있는지
                    onBridge.append(trucks.popleft())
                else:  
                    onBridge.append(0)        
            elif sum(onBridge)==max(onBridge):          # 남은 거 한번에 계산
                answer += onBridge.index(max(onBridge))+1
                break                
            # print(answer, onBridge, trucks)
    return answer
    

### deque.함수들
    # maxlen
    # append
    # appendleft
    # pop
    # popleft
    # rotate


### 옛날 풀이 개선
    
    answer = 0
    bridge = [0]*bridge_length             # 다리를 지나는 트럭
    # 이걸 비울 때까지 반복(무게 초과할 때 0 넣지만 trucks 다 올라오면 안 넣음 -> 마지막은 0이 아닐 것
    trucks = deque(truck_weights)
    
    t = 0
    while bridge:
        t += 1
        
        bridge.pop(0)
        if trucks:
            if sum(bridge) + trucks[0] <= weight:
                bridge.append(trucks.popleft())     # 트럭 진입
            else:
                bridge.append(0)                          
            
    return t
    
     
### 옛날 풀이 (못품)    
    
    answer = 0
    bridge = []             # 다리를 지나는 트럭
    # bridge_weight = 0       # 다리를 지나는 트럭의 무게
    # bridge_len = 0       # 다리를 지나는 트럭의 무게
    trucks = deque(truck_weights)
    
    print(trucks)
    # print(dir(deque))
    t = 0
    while trucks:
        t += 1
        
        if len(bridge) == bridge_length:
            bridge.pop()
            # bridge_len -= 1
        # truck = trucks[0]
        # truck = truck_weights.popleft()
        if sum(bridge) + trucks[0] < weight:
            bridge.append(trucks.popleft())     # 트럭 진입
            # bridge_weight += truck
            # bridge_len += 1
        else:
            bridge.append(0)
            # bridge_len += 1            
            
    answer = t + len(bridge) + bridge_length - 1
    return answer

