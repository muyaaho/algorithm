n, m = map(int, input().split())

def dfs(arr, cnt):
    if cnt == m:
        print(*arr)
        return
    
    for i in range(arr[-1], n+1):
        arr.append(i)
        dfs(arr, cnt + 1)
        arr.pop()

for i in range(1, n+1):
    arr = [i]
    dfs(arr, 1)