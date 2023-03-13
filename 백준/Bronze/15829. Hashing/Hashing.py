n = int(input())
s = input()

ans = 0
for i, x in enumerate(s):
    ans += (ord(x)-ord('a')+1)*31**i

print(ans)