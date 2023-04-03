from collections import Counter
import sys

n = int(sys.stdin.readline().rstrip())
nums = list(map(int,sys.stdin.readline().rstrip().split(' ')))
v = int(sys.stdin.readline().rstrip())

print(Counter(nums)[v])

