import re

regex = '[A-Z][a-z]*'
target = input()
results = re.findall(regex, target)
answer = 0
for i in range(len(results)-1):
    r = len(results[i])%4
    answer += 4-r if r>0 else 0
print(results)
print(answer)