# 크로아티아 알파벳

# s = input()
# cro = ['c=','c-','dz=','d-','lj','nj','s=','z=']
# regex = '[\\c=|\\c-|\dz=|\d-|\lj|\\nj|\\s=|\\z=|a-z]'
# result = re.findall(regex, s)
# print(result)
# print(len(result))

s = input()
# cro = {'c=':1,'c-':1,'dz=':2,'d-':1,'lj':1,'nj':1,'s=':1,'z=':1}
cro = ['c=','c-','dz=','d-','lj','nj','s=','z=']
answer = 0
continue_ = 0
for i in range(len(s)):
    if continue_>0:
        continue_ -= 1
        continue 
    if s[i] in 'cdlnsz':
        if s[i:i+2] in cro:
            continue_ = 1
        elif s[i:i+3] in cro:
            continue_ = 2
        answer += 1            
    else:
        answer += 1

print(answer)