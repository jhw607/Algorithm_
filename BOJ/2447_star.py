def func(n):

    if n == 3:
        return ['***', '* *', '***']
    
    iter = n//3
    arr = func(iter)
    stars = []

    for i in arr:
        stars.append(i*3)
    for i in arr:
        stars.append(i + ' '*iter + i)
    for i in arr:
        stars.append(i*3)

    return stars


num = input()
print(num)
answer = func(int(num))
print(answer)





# def func(x, y, n, flag):

#     if x == n or y == n:
#         return
    
#     iter = n%3+1

#     if (iter <= x%3 < iter*2) and (iter <= y%3 < iter*2):
#         answer[x][y] = func(x, y, n, False)

# num = int(input())
# answer = []