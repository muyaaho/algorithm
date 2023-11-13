n = int(input())
arr = [0] + [int(input()) for _ in range(n)]
dp = [0] * (n+1)
if n < 3:
    print(sum(arr))
    exit(0)
dp[1] = arr[1]
dp[2] = arr[1] + arr[2]
dp[3] = max(dp[1]+arr[3], arr[2]+arr[3])

for i in range(4, n+1):
    dp[i] = max(arr[i-1] + dp[i-3] + arr[i], dp[i-2] + arr[i])
    # print(dp)
print(dp[n])