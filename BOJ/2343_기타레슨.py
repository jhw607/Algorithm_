n, m = map(int, input().split(' '))
lessons = list(map(int, input().split(' ')))

left, right = min(lessons), sum(lessons)

while left<right:
    mid = (left+right)//2
    
    i = 0
    blue = [0]
    for lesson in lessons:
        if lesson>mid:
            left = lesson
            break
        if blue[i]+lesson<=mid:
            blue[i] += lesson
        else:
            blue.append(lesson)
            i+=1
    else:         
        if len(blue)>m:
            left = mid+1
        else:
            right = mid
tmp = left

# left, right = min(lessons), sum(lessons)
# while left<right:
#     mid = (left+right)//2
    
#     i = 0
#     blue = [0]
#     for j in range(n-1, -1, -1):
        
#         if blue[i]+lessons[j]<=mid:
#             blue[i] += lessons[j]
#         else:
#             blue.append(lessons[j])
#             i+=1
            
#     if len(blue)>m:
#         left = mid+1
#     else:
#         right = mid

# tmp = min(tmp, left)

print(tmp)