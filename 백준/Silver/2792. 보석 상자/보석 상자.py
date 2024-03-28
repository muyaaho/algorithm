import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [int(input()) for _ in range(m)]

start = 1
end = max(arr)

answer = 0
isN = False
while start <= end:
    mid = (start + end) // 2
    
    cnt = 0
    for x in arr:
        if x % mid:
            cnt += x // mid + 1
        else:
            cnt += x // mid

    if cnt > n:
        start = mid + 1
        
    else:
        end = mid -1
        answer = mid

print(answer)