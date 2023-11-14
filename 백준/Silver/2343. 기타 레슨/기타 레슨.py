n, m = map(int, input().split())
arr = list(map(int, input().split()))

start = max(arr)
end = sum(arr)

while start <= end:
    mid = (start + end)//2
    cnt, s = 0, 0
    
    for x in arr:
        if s+x > mid:
            cnt += 1
            s = 0
        s += x
    if s:
        cnt += 1
    
    if cnt > m:
        # 자른 것 보다 갯수가 많이 나오면 너무 작게 잘랐다는 말임. (분이 작다) 그래서 start
        start = mid+1
    else:
        end = mid-1
print(start)