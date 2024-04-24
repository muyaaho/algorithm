import sys
input = sys.stdin.readline

def dfs(cnt, s, tmp):
    global answer
    if cnt == 4:
        answer = max(answer, s)
        return
    
    for x, y in tmp:
        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nx, ny = dx + x, dy + y
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                visited[nx][ny] = True
                dfs(cnt + 1, s + arr[nx][ny], tmp + [(nx, ny)])
                visited[nx][ny] = False
                
            

n, m = map(int, input().split())    
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

answer = 0

for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(1, arr[i][j], [(i, j)])

print(answer)