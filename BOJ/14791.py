n = int(input())
nums = list(int(input()) for _ in range(n))
answer = []
std = 0
for num in nums:
    # for number in range(num, 0, -1):
    number = num
    while True:
        arr = list(str(number))
        for i in range(0, len(arr)-1):
            if int(arr[i]) > int(arr[i+1]): 
                std = len(arr) - i -1
                arr = arr[:i]+[str(int(arr[i])-1)]+['9'*std]
                number = int(''.join(arr))
                break            
        else:
            answer.append(number)
            break
        
# for num in nums:
#     for number in range(num, 0, -1):
#         arr = list(str(number))
#         for i in range(0, len(arr)-1):
#             # print(number, arr, arr[i], arr[i-1])
#             if arr[i] > arr[i+1]: break            
#         else:
#             answer.append(number)
#             break

for i in range(n):
    print(f"Case #{i+1}:", answer[i])











