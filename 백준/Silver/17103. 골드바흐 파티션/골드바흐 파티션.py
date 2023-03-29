import sys
input = sys.stdin.readline

t = int(input())
arr = [int(input()) for _ in range(t)]

# 에라토스테네스의 체
m = max(arr)
a = [False, False] + [True] *(m-1)
primes = []


for i in range(2, m+1):
    if a[i]:
        primes.append(i)
        for j in range(2*i, m+1, i):
            a[j] = False


for n in arr:
    ans = 0
    for i in primes:
        if i>=n:
            break
        if a[n-i] and i <= n-i:
            ans += 1
    
    print(ans)

