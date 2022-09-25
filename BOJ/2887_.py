from itertools import combinations

def find(a):
    if parent[a] == a:
        return a
    return find(parent[a])

def union(a,b):

    p_a = find(a)
    p_b = find(b)


    return

def calc(a,b):
    x = abs(a[0]-b[0]),
    y = abs(a[1]-b[1])
    z = abs(a[2]-b[2])
    return min(x,y,z)


n = int(input())
parent = [i for i in range(n)]
positions = []

for i in range(n):
    x, y, z = map(int, input().split(' '))
    positions.append((x,y,z,i))


print(positions)
