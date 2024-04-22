import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
dp = [INF] * (n+1)

dp[0] = 0
dp[1] = 1

d = 1
for i in range(2, n+1):
    d = int(i ** (1/2))
    for j in range(d, d//2, -1):
        dp[i] = min(dp[i], dp[i - j**2] + 1)
# print(dp)
print(dp[n])