import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

start = min(arr)
end = sum(arr)

while start <= end:
    mid = (start + end)//2
    charge = mid
    cnt = 1
    
    for money in arr:
        if money > charge:
            cnt += 1
            charge = mid
        charge -= money
    
    
    if cnt > m or mid < max(arr):
        start = mid+1
    else:
        end = mid-1
        answer = mid
print(answer)