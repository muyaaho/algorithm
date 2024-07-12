n = int(input())

dp = dict()

def sol(n):
    if dp.get(n) != None:
        return dp[n]
    
    if n == 0:
        return 0
    
    if n == 1 or n == 2:
        return 1
    
    dp[n//2 + 1] = sol(n//2 + 1) % 1_000_000_007
    if n % 2 == 0:
        dp[n//2 - 1] = sol(n//2 - 1) % 1_000_000_007
        return (dp[n//2+1] ** 2 - dp[n//2-1] ** 2) % 1_000_000_007
    else:
        dp[n//2] = sol(n//2) % 1_000_000_007
        return (dp[n//2+1] ** 2 + dp[n//2] ** 2) % 1_000_000_007
print(sol(n))