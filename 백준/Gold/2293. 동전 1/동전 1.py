n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()

dp = [0] * (k+1)
dp[0] = 1
for money in arr:
    for i in range(money, k+1):
        dp[i] += dp[i-money]

print(dp[k])