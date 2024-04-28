import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
mx = max(map(max, arr))

answer = 0
def dfs(cnt, s, tmp):
    global answer
    if s + (4-cnt) * mx <= answer:
        return
    
    if cnt == 4:
        answer = max(s, answer)
        return
    
    for x, y in tmp:
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                visited[nx][ny] = True
                dfs(cnt + 1, s + arr[nx][ny], tmp + [(nx, ny)])
                visited[nx][ny] = False

visited = [[False] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(1, arr[i][j], [(i, j)])

print(answer)