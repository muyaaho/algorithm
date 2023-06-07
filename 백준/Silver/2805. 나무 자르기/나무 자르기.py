import sys
input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))

start = 0
end = max(trees)

ans = 0
while start <= end:
    cut = 0
    mid = (start+end) // 2
    
    for tree in trees:
        if tree > mid:
            cut += tree - mid
    
    if cut < M:
        end = mid - 1
    else:
        ans = mid
        start = mid + 1

print(ans)