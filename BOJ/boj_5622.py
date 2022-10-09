# print(ord('P'))
# print(ord('S'))

words = input()
answer = 0
for word in words:
    num = ord(word)
    if num<68: answer += 3
    elif num<71: answer += 4
    elif num<74: answer += 5
    elif num<77: answer += 6
    elif num<80: answer += 7
    elif num<84: answer += 8
    elif num<87: answer += 9
    else: answer += 10
    
print(answer)