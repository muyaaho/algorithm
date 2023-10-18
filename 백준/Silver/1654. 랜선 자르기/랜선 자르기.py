import sys
input = sys.stdin.readline

# 이미 갖고 있는 랜선 k, 필요한 랜선 n
k, n = map(int, input().split())
arr = [int(input()) for _ in range(k)]
arr.sort()

'''
떡볶이 떡 문제를 생각하면서 풀어보자

'''
start = 1
end = max(arr)

answer = 0
while start <= end:
    # print(f'start, end: {start} {end}')
    cnt = 0
    mid = (start + end)//2
    # print(f'mid: {mid}')
    for x in arr:
        if x >= mid:
            cnt += x//mid
    # print(f'cnt: {cnt}')
    # 필요한 랜선보다 만들어진게 적다면 mid를 더 작게!
    if cnt < n:
        end = mid-1
    else:
        answer = mid
        start = mid+1

print(answer)