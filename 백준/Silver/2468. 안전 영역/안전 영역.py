from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
arr = []
max_level = -1
# min_level = 1e9
for _ in range(n):
    line = list(map(int, input().split()))
    max_level = max(max_level, max(line))
    # min_level = min(min_level, min(line))
    arr.append(line)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(level, x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    isNext = False
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and arr[nx][ny] > level:
                    isNext = True
                    visited[nx][ny] = True
                    q.append((nx, ny))

    return isNext

answer = 0

for level in range(max_level):
    count = 0
    visited = [[False] * (n) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and arr[i][j] > level:
                bfs(level, i, j)
                count += 1
    
    answer = max(answer, count)
print(answer)