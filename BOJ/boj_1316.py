# from collections import defaultdict

n = int(input())
words = [input() for _ in range(n)]
cnt = 0
for word in words:
    char = set()
    before = ''
    for ch in word:
        if ch == before:
            continue
        if ch in char:
            break
        char.add(ch)
        before = ch
    else:
        cnt += 1
print(cnt)