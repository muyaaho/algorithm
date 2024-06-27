import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

l, r, cnt, kind, m = 0, 0, 0, 0, 0
nums = [0] * 10

while r < n:
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
    r += 1

print(m)