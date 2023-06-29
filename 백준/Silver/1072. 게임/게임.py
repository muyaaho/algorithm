import sys
input = sys.stdin.readline

x, y = map(int, input().split())
z = y*100//x

ans = sys.maxsize
l, r = 1, x

while l<=r:
    mid = (l+r)//2
    
    curr_z = (y+mid) * 100 // (x+mid)
    
    if curr_z > z:
        ans = min(mid, ans)
        r = mid - 1
    else:
        l = mid + 1

if ans == sys.maxsize:
    print(-1)
else:
    print(ans)