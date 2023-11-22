from bisect import bisect_left
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dp = []
for x in arr:
    k = bisect_left(dp, x)
    if k >= len(dp):
        dp.append(x)
    else:
        dp[k] = x
print(len(dp))