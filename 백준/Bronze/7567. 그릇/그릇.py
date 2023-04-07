n = input()

ans = 10
before = n[0]
for x in n[1:]:
    if before == x:
        ans += 5
    else:
        ans += 10
    before = x

print(ans)