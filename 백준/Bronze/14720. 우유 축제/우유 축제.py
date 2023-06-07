n = int(input())
arr = list(map(int, input().split()))

milk = [0, 1, 2]
ans = 0
idx = 0
for x in arr:
    if x == milk[idx]:
        ans += 1
        idx = (idx+1)%3

print(ans)