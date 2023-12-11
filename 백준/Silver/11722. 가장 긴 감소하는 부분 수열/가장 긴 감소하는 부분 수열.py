import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
rarr = arr[::-1]

dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if rarr[i] > rarr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))