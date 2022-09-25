

n = input()
words = input()
flag = False
tmp = []
for word in words:
    if word.isdigit():
        if flag:
            tmp[-1] += word
        else:
            tmp.append(word)
        flag = True
    else:
        flag = False


print(sum(map(int, tmp)))