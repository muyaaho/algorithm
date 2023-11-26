n = int(input())
arr = list(map(int, input().split()))
rarr = arr[::-1]

dp1 = [1] * n
dp2 = [1] * n

for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp1[i] = max(dp1[i], dp1[j] + 1)
        if rarr[i] > rarr[j]:
            dp2[i] = max(dp2[i], dp2[j] + 1)

result = [dp1[i] + dp2[n-i-1]-1 for i in range(n)]
print(max(result))