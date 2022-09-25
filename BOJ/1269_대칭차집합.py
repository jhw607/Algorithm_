
a, b = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

a_prime = A-B
b_prime = B-A
# answer = list(a_prime) + list(b_prime)
answer = a_prime|b_prime
# print(len(set(answer)))
print(len(answer))