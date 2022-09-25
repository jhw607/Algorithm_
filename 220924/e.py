cap = 4
n = 5
deliveries = [1,0,3,1,2]
pickups = [0,3,0,4,0]

answer = 0
next_del, next_pick = n-1, n-1
for i in range(n-1, -1, -1):
    if deliveries[i]>0:
        next_del = i
        break
for i in range(n-1, -1, -1):
    if pickups[i]>0:
        next_pick = i
        break

# box_del = sum(deliveries)
# box_pick = sum(pickups)

truck = 0
while sum(deliveries)>0 or sum(pickups)>0:
    dest = max(next_del, next_pick)
    truck = 0
    answer += (dest+1)*2
    for i in range(next_del, -1, -1):
        print('del', next_del, i, truck)
        print(deliveries)
        if truck + deliveries[i] <= cap:
            print('yes', i)
            truck += deliveries[i]
            deliveries[i] = 0
            next_del = i-1 if i>0 else 0
        else:
            deliveries[i] -= cap - truck
            truck = cap
            next_del = i
            break
    print('side: ', truck)
    truck = 0
    for i in range(next_pick, -1, -1):
        print('pick', next_pick, i, truck)
        print(pickups)
        if truck + pickups[i] <= cap:
            truck += pickups[i]
            pickups[i] = 0
            next_pick = i-1 if i>0 else 0
        else:
            pickups[i] -= cap - truck
            truck = cap
            next_pick = i
            break
    print('end of while')
    print(deliveries)
    print(pickups)
    
print(answer)