a, b, c = map(int, input().split())
d = int(input())

a += d//3600
d %= 3600

b += d//60
c += d%60

if c >= 60:
    b += 1
    c %= 60
if b >= 60:
    a += 1
    b %= 60
if a >= 24:
    a %= 24

print(a, b, c)