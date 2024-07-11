import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = sorted(map(int, input().split()))
visited = [False] * n

def sol(tmp):
    if len(tmp) == m:
        print(*tmp)
        return
    
    past = 0
    for i in range(n):
        if not visited[i] and arr[i] != past:
            visited[i] = True
            past = arr[i]
            tmp.append(arr[i])
            sol(tmp)
            visited[i] = False
            tmp.pop()

sol([])