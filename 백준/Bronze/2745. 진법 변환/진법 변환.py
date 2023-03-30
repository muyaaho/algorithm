n, b = input().split()
b = int(b)
overnum = {chr: num for num, chr in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ', start = 10)}
# print(overnum)

ans = 0
for i, x in enumerate(n[::-1]):
    if x.isalpha():
        x = overnum[x]
    else:
        x = int(x)
    
    if i == 0:
        ans += x
    else:
        ans += (b**i)*x

print(ans)