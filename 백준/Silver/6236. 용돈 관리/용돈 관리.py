import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

start = 0
end = sum(arr)

answer =0
while start <= end:
    mid = (start + end)//2
    s = mid
    cnt = 1
    
    for money in arr:
        if s < money:
            cnt += 1
            s = mid
        s -= money
        # print(s)
    
    if cnt > m or mid < max(arr):
        start = mid+1
    else:
        end = mid-1
        answer = mid
print(answer)