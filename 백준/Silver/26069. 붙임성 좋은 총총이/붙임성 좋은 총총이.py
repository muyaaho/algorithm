n = int(input())

arr = []
for _ in range(n):
    arr.append(input().split())

check = set()

ans = 0
for a, b in arr:
    if a == "ChongChong":
        if b not in check:
            check.add(b)
            ans += 1
        if a not in check:
            check.add(a)
            ans += 1
    elif b == "ChongChong":
        if a not in check:
            check.add(a)
            ans += 1
        if b not in check:
            check.add(b)
            ans += 1
    elif a in check:
        if b not in check:
            check.add(b)
            ans += 1
    elif b in check:
        if a not in check:
            check.add(a)
            ans += 1
print(ans)