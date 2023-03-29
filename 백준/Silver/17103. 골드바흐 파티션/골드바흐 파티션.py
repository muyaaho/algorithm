import sys
input = sys.stdin.readline

# t = int(input())

# 에라토스테네스의 체
m = 1000000
a = [False, False] + [True] *(m-1)
# primes = []


for i in range(2, m+1):
    if a[i]:
        # primes.append(i)
        for j in range(2*i, m+1, i):
            a[j] = False

for _ in range(int(input())):
    n = int(input())
    # 에스토스테네스의 체까지 가는 방법? 작으면 break 하기?

    ans = 0
    for i in range((n//2)+1):
        if a[i] and a[n-i]:
            ans += 1
    
    print(ans)