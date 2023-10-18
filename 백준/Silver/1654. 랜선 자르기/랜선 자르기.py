import sys
input = sys.stdin.readline

# 이미 갖고 있는 랜선 k, 필요한 랜선 n
k, n = map(int, input().split())
arr = [int(input()) for _ in range(k)]

start = 1
end = max(arr)

answer = 0
while start <= end:
    cnt = 0
    mid = (start + end)//2
    for x in arr:
        cnt += x//mid
        
    if cnt < n:
        end = mid-1
    else:
        answer = mid
        start = mid+1

print(answer)