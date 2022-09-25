
def func(x, y, n):
    # if y>num: return
    iter = n%3+1
    if n==3:
    #     print('1')
        # print('iter : ', iter)
        # for i in range(n):
        if iter <= x%3 < iter*2 and iter <= y%3 < iter*2:            
            print('2', x, y, n)
            # answer[x][y]+=('*'*iter)
            answer[x]+='   '
            answer[x] = ''.join(answer[x])
            # answer[x][y]+=('*'*iter)
            # return
        elif not (iter <= x%3 < iter*2) and not (iter <= y%3 < iter*2): 
            print('4', x, y, n)
            # answer[x][y]+=('*'*iter)
            answer[x]+='***'
            answer[x] = ''.join(answer[x])
        elif (not (iter <= x%3 < iter*2) and (iter <= y%3 < iter*2)) or ((iter <= x%3 < iter*2) and not(iter <= y%3 < iter*2)): 
            print('4', x, y, n)
            # answer[x][y]+=('*'*iter)
            answer[x]+='* *'
            answer[x] = ''.join(answer[x])
        else :
            print('5', x, y, n)
            answer[x]+='***'
            answer[x] = ''.join(answer[x])

        #     print('5', x, y, n)
        #     answer[x]+='***'
        #     answer[x] = ''.join(answer[x])
        #     # print('4', x, y, n)
        #     # answer[x][y]+=('*')
        #     # answer[x][y]+=('*'*iter)
        #     # answer[x][y]+=('*'*iter)
        #     # return
    else:
        for j in range(n):  # 0 1 2
            for k in range(n//3):
                if iter <= j%3 < iter*2 and iter <= k%3 < iter*2:      
                    print('0')
                    answer[j]+='   '
                    ''.join(answer[j])
                else:
                    print('1')
                    func(j, k, n//3)

num = int(input())
# iter = n//3
answer = ['']*num
# print(answer)
func(0, 0, num)


# for j in range(num//3):  # 0 1 2
#     for k in range(num//3):
#         func(j, k, num//3, num)

print(answer)  
# print(answer[:num//3][:num//3])  

# for i in range(n):
#     if n//3 <= i < n*2//3: 
#         print('*'*iter, end='')
#         print(' '*iter, end='')
#         print('*'*iter)
#     else:
#         print('*'*n)
    

        # if iter <= x%3 < iter*2:
        #     if iter <= y%3 < iter*2 : 
        #         print('2', x, y, n)
        #         # answer[x][y]+=('*'*iter)
        #         answer[x]+=' '*3
        #         answer[x] = ''.join(answer[x])
        #         # answer[x][y]+=('*'*iter)
        #         # return
        #     else:
        #         print('3', x, y, n)
        #         answer[x]+='*'*3
        #         answer[x] = ''.join(answer[x])
        # else:
        #     if iter <= y%3 < iter*2 : 
        #         print('4', x, y, n)
        #         # answer[x][y]+=('*'*iter)
        #         answer[x]+='* *'
        #         answer[x] = ''.join(answer[x])
        #         # answer[x][y]+=('*'*iter)
        #         # return
        #     else:
        #         print('5', x, y, n)
        #         answer[x]+='*'*3
        #         answer[x] = ''.join(answer[x])
        #     # print('4', x, y, n)
        #     # answer[x][y]+=('*')
        #     # answer[x][y]+=('*'*iter)
        #     # answer[x][y]+=('*'*iter)
        #     # return