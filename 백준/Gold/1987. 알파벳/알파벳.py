r, c = map(int, input().split())
arr = [list(input()) for _ in range(r)]

s = set()
answer = 1
s.add(arr[0][0])

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(x, y, cnt):
    global answer
    
    answer = max(answer, cnt)
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and not arr[nx][ny] in s:
            s.add(arr[nx][ny])
            dfs(nx, ny, cnt+1)
            s.remove(arr[nx][ny])

dfs(0, 0, 1)
print(answer)