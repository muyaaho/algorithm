import sys
input = sys.stdin.readline

a = input().rstrip()
b = input().rstrip()

width = len(a)+1
length = len(b)+1

dp = [[0] * length for _ in range(width)]

for i in range(1, width):
    for j in range(1, length):
        if a[i-1] == b[j-1]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])