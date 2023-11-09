import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
ans = abs(100-n)
broken = set(input().split()) if m else set()

for num in range(1000001):
    for chr in str(num):
        if chr in broken:
            break
    else:
        ans = min(ans, len(str(num)) + abs(n-num))
print(ans)