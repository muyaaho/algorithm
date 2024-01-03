import sys

input = sys.stdin.readline

# 조카의 수, 과자의 수
m, n = map(int, input().split())
arr = list(map(int, input().split()))

start = 1
end = max(arr)

answer =0 
while start <= end:
    mid = (start + end) // 2

    cnt = 0
    for x in arr:
        if x >= mid:
            cnt += x // mid

    if cnt < m:
        end = mid - 1

    else:
        answer = mid
        start = mid + 1
print(answer)
