from collections import deque
n = int(input())

maps = [list(map(int, input())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = []
def bfs(x, y, cnt):
    q = deque()
    q.append((x, y))
    ans = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < n and 0 <= ny < n and maps[nx][ny] == 1:
                maps[nx][ny] = cnt*10
                q.append((nx, ny))
                ans += 1
    answer.append(ans)

cnt = 1
for i in range(n):
    for j in range(n):
        if maps[i][j] == 1:
            maps[i][j] = cnt*10
            bfs(i, j, cnt)
            cnt += 1

print(len(answer))
answer.sort()
print(*answer, sep='\n')