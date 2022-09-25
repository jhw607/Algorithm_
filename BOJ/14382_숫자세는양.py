t = int(input())
nums = [int(input()) for _ in range(t)]
answer = []

for num in nums:
    n, i = num, 0
    sleep = ['0','1','2','3','4','5','6','7','8','9']
    while sleep:
        if num == num*2:
            answer.append("INSOMNIA")
            break
        # print('num :',num)
        i = num
        tmp = str(num)
        for s in tmp:
            # print('s :',s)
            if s in sleep:
                sleep.remove(s)
        i += 1
        num += n
    else:
        answer.append(num-n)

for i, ans in enumerate(answer):
    print(f"Case #{i+1}:",ans)
# print(answer)
