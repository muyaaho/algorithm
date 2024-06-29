import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = sorted(map(int, input().split()))
visited = [False] * n

tmp = []
def dfs():
    if len(tmp) == m:
        print(*tmp)
        return
    past = -1
    
    for i in range(n):
        if not visited[i] and past != arr[i]:
            past = arr[i]
            visited[i] = True
            tmp.append(arr[i])
            dfs()
            visited[i] = False
            tmp.pop()
dfs()