
words = input()
m = int(input())
instructions = [input() for _ in range(m)]

# cursor = len(words) # 0~n : n+1가지
# left = list(words)
right = ''

for instruction in instructions:
    if instruction == 'L':
        if words:
            right = words[-1] + right
            words = words[:-1]
            # right = (words.pop())
        # cursor = cursor - 1 if cursor!=0 else cursor
    elif instruction == 'D':
        if right:            
            words = words + right[0]
            right = right[1:]
            # words.append(right.pop())
        # cursor = cursor + 1 if cursor!=len(words) else cursor
    elif instruction == 'B':
        if words:
            words = words[:-1]
            # words.pop()
        # if cursor != 0:
        #     words = words[:cursor-1] + words[cursor:]
        #     cursor -= 1
    else:
        word = instruction.split(' ')[1]
        words = words + word
        # words.append(word)
        # if cursor != 0:
        #     words = words[:cursor]+word+words[cursor:]
        # else:
        #     words = word+words
        # cursor += 1
words = words+right
print(words)