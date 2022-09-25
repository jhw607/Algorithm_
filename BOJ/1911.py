n, l = map(int, input().split(' ')) # n:웅덩이, l:널빤지
puddles = [tuple(map(int, input().split(' '))) for _ in range(n)]
ans = 0

puddles.sort()
stk = []
start = puddles[0][0]
tree = start+l
for s,e in puddles:
    
    # cnt, left = divmod(puddle, l)
    # ans += cnt

    if tree <= s:
        tree = s+l
        # end = start+l
        ans +=1
    if tree<e:

        cnt, left = divmod(e-tree, l)
        if left:
            tree = e+left
            ans += cnt+1
        else:
            tree = e
            ans += cnt
        # end = start+l
    print(ans)

print(ans)













# puddles.sort()
# start = puddles[0][0]
# end = start+l
# for s, e in puddles:
#     if start <= s:
#         start = s+l
#         # end = start+l
#         ans +=1
#     while e-start>0:
#         ans += 1
#         start += l
#         # end = start+l
#     print(ans)