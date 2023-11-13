n, m = map(int, input().split())
arr = list(map(int, input().split()))

start = max(arr)
end = sum(arr)

while start <= end:
    mid = (start+end)//2
    
    cnt, s = 0, 0
    for x in arr:
        if x + s > mid:
            cnt += 1
            s = 0
        s += x
    if s:
        cnt += 1
    
    if cnt <= m:
        end = mid-1
    else:
        start = mid + 1
        
print(start)