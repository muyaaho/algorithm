import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
arr = list(map(int, input().split()))

nums = [0] * 10
def sol(l, r, cnt, kind, m):
    if r == n:
        return m
    
    if nums[arr[r]] == 0:
        kind += 1
    cnt += 1
    nums[arr[r]] += 1
    
    if kind > 2:
        nums[arr[l]] -= 1
        if nums[arr[l]] == 0:
            kind -= 1
            
        cnt -= 1
        l += 1
    
    m = max(m, cnt)
    return sol(l, r+1, cnt, kind, m)

print(sol(0, 0, 0, 0, 0))