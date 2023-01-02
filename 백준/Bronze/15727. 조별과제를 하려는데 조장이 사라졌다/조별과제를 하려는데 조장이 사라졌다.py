n = int(input())
a = 0
for x in range(5, 0, -1):
    a += n//x
    n %= x

print(a)