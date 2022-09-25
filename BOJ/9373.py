from math import sqrt


t = int(input())    # 테스트케이스 수
cases = []
for _ in range(t):
    # w = int(input())    # 복도의 너비
    # n = int(input())    # 센서의 개수
    # sensors = [tuple(map(int, input().split(' '))) for _ in range(n)]
    # cases.append((w, n, sensors))
    cases.append([int(input()), [list(map(int, input().split(' '))) for _ in range(int(input()))]])

print(cases)
answer = []
while cases:
    w, sensors = cases.pop(0)
    n = len(sensors)
    sensors.sort(key=lambda x:x[1])
    # y축 기준으로 정렬
    print(sensors)
    # (두 중심의 거리 - 반지름 합) 의 최솟값
    x1, y1, r1 = sensors[0]
    tmp = w
    c = x1+r1 if x1<w//2 else w-x1+r1
    if c<w:
        tmp = min(tmp, c)
    else:
        answer.append(0)
        continue

    for i in range(1, n):
        x2, y2, r2 = sensors[i]
        dist = sqrt(abs(x2-x1)**2 + abs(y2-y1)**2)
        rr = r1+r2
        size = dist - rr
        if x2<w//2:
            c = x2+r2
        else:
            c = w-x2+r2
        print(c)
        if size > 0 and c < w:
            tmp = min(tmp, size) if size<c else min(tmp,c)
        else:
            break
    else:
        answer.append(tmp)
        x1,y1,r1 = x2, y2, r2
        continue
    answer.append(0)
        
print(answer)
