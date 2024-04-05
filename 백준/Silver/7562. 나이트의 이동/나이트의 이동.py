from collections import deque
import sys
input = sys.stdin.readline

INF = int(1e9)
move = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)]

for _ in range(int(input())):
    l = int(input())
    nx, ny = map(int, input().split())
    tx, ty = map(int, input().split())
    
    q = deque()
    q.append((nx, ny))
    visited = [[INF] * l for _ in range(l)]
    visited[nx][ny] = 0
    
    while q:
        x, y = q.popleft()
        
        for px, py in move:
            dx = x + px
            dy = y + py
            
            if 0 <= dx < l and 0 <= dy < l and visited[dx][dy] == INF:
                visited[dx][dy] = visited[x][y] + 1
                q.append((dx, dy))
    
    print(visited[tx][ty])