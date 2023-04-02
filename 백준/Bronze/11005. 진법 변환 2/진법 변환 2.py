import sys
input = sys.stdin.readline

n, b = map(int, input().split())
overnum = {num:chr for num, chr in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ', start = 10)}

ans = []
while n!=0:
    rmd = n%b
    if rmd > 9:
        ans.append(overnum[n%b])
    else:
        ans.append(str(rmd))
    n //= b

# if n > 9:
#     ans.append(overnum[n])
# else:
#     ans.append(str(n))

print("".join(ans[::-1]))