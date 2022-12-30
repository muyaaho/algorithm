n, k = map(int, input().split())
a = [int(input()) for _ in range(n)]

count = 0
for money in a[::-1]:
    if k>=money:
        count += k//money
        k %= money
    if k<=0: break

print(count)