from collections import deque
from heapq import heappush, heappop
import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            bx, by = i, j
            break

dx = [-1, 0,1 , 0]
dy = [0, -1, 0, 1]

target = 2
eat_count = 0
answer = 0

def bfs(sx, sy):
    q = deque()
    q.append((sx, sy))
    visited = [[-1] * n for _ in range(n)]
    visited[sx][sy] = 0
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if (0 <= nx < n and 0 <= ny < n) and arr[nx][ny] <= target and visited[nx][ny] < 0:
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
    
    return visited

while True:
    
    dist_map = bfs(bx, by)
    dist = []
    can_eat = 0
    
    for i in range(n):
        for j in range(n):
            if arr[i][j] < target and arr[i][j] > 0 and dist_map[i][j] > 0:
                heappush(dist, (dist_map[i][j], i, j))
    
    if not dist:
        print(answer)
        break
    
    _, ex, ey = heappop(dist)
    answer += dist_map[ex][ey]
    eat_count += 1
    
    if eat_count == target:
        target += 1
        eat_count = 0
    
    arr[ex][ey] = 9
    arr[bx][by] = 0
    bx, by = ex, ey