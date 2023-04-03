def facto(i):
    if i <= 1:
        return 1
    return i*facto(i-1)

print(facto(int(input())))