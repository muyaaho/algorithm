n, k = map(int, input().split())

arr = [int(input()) for _ in range(n)]

dp = [10001] * (k+1)
dp[0] = 0
for i in range(n):
    for j in range(arr[i], k + 1):
        if dp[j - arr[i]] != 10001:
            dp[j] = min(dp[j], dp[j - arr[i]] + 1)

print(-1 if dp[k] > 10000 else dp[k])