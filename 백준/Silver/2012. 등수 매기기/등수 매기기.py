import sys
input = sys.stdin.readline

n = int(input())
arr = list(int(input()) for _ in range(n))

arr.sort()

ans = 0
for i, x in enumerate(arr, start=1):
    ans += abs(i-x)

print(ans)