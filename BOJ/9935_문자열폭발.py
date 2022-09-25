string = input()
boom = input()
n, m = len(string), len(boom)
tmp = ''


while string:
    if boom not in string:
        break
    # n, m = -1, -1
    # if string[n] == boom[m]:
    if string[-m:] == boom:
        string = string[:-m] + tmp
        tmp = ''
        # string = string[:-m] + tmp[0]
        # tmp = tmp[1:]
    else:
        tmp = string[-1]+tmp
        string = string[:-1]
    # print(string)

if string:
    print(string)
else:
    print('FRULA')






# ----- 시간초과 -----
# 
# while boom in string:
#     idx = string.index(boom)
#     string = string[:idx] + string[idx+len(boom):]

# if string:
#     print(string)
# else:
#     print('FRULA')