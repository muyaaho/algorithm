import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
broken = set(input().split()) if m else set()
ans = abs(100-n)

for nums in range(1_000_001):
    for num in str(nums):
        if num in broken:
            break
    else:
        ans = min(ans, len(str(nums)) + abs(n - nums))

print(ans)