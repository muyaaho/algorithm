s, d = map(int, input().split())

a = (s+d)/2
if a%1 > 0 or s+d < 0 or s-d < 0:
    print(-1)
else:
    a = int(a)
    print(a, s-a)
