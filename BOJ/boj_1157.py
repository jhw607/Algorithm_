# print(chr(90))
# print(chr(97)) # +- 32

from collections import Counter, defaultdict
# sol1                              148ms
# s = input()
# chars = Counter(list(s))
# # print(chars)
# res = defaultdict(int)
# # print(res)
# max_cnt = 0
# max_ch = ''
# for i in range(65, 91):
#     ch = chr(i)
#     if ch in chars.keys():
#         res[ch] += chars[ch]
#     ch_ = chr(i+32)
#     if ch_ in chars.keys():
#         res[ch] += chars[ch_]
# # print(res.items())

# result = list(res.items())
# result.sort(key=lambda x:x[1])
# if len(s)>1 and result[-1][1] == result[-2][1]:
#     print('?')
# else:
#     print(result[-1][0])

# sol2                              156ms
s = input()
chars = Counter(list(s.upper()))

result = list(chars.items())
result.sort(key=lambda x:x[1])
if len(s)>1 and result[-1][1] == result[-2][1]:
    print('?')
else:
    print(result[-1][0])