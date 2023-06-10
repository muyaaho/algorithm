changes = [500, 100, 50, 10, 5, 1]

n = int(input())
a = 1000-n

ans = 0
for x in changes: 
    ans += a//x
    a = a%x

print(ans)