import sys
input = sys.stdin.readline

s = set()

n , m = map(int, input().split())
arr = sorted(map(int, input().split()))
ans = set()
def dfs(x, tmp, cnt):
    if cnt == m:
        ans.add(tuple(tmp))
        return
    
    for k in arr:
        if (tmp[-1] > k):
            continue
        t = tuple(tmp+[k])
        if t not in s:
            s.add(t)
            dfs(k, tmp+[k], cnt+1)
            s.remove(t)
            

for i in set(arr):
    dfs(i, [i], 1)

for line in sorted(ans):
    print(*line)