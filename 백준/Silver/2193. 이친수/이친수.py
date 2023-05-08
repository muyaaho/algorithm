n = int(input())

dp = [0]*(100)
# dp = [0,1,1,2]
dp[0] = 0
dp[1] = 1
dp[2] = 1
dp[3] = 2

for i in range(4, n+1):
    dp[i] = 2*dp[i-2] + 1*dp[i-3]
# else:
#     for i in range(4, 91):
#         dp[i] = dp[i-1] + dp[i-2]

# print(dp)
print(dp[n])