import sys

t = int(sys.stdin.readline().rstrip())
[print(sum(map(int, sys.stdin.readline().rstrip().split(' ')))) for _ in range(t)]
