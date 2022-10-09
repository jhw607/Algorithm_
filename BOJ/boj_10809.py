# 알파벳 찾기
# from email import charset
import re
# from xml.dom.pulldom import CHARACTERS

s = input()

answer = []
for ch in 'abcdefghijklmnopqrstuvwxyz':
    
    # sol1
    # answer.append(s.find(ch))   # 68ms
    # sol2-1
    if ch in s:                 # 68ms
    # sol2-2
    # if re.search(ch,s):       # 132ms
        answer.append(s.index(ch))
    else:
        answer.append(-1)
print(*answer)