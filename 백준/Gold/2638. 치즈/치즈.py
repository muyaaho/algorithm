from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs():
    q = deque()
    q.append((0, 0))
    visited = [[0] * m for _ in range(n)]
    visited[0][0] = 1
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == 0 and arr[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                elif arr[nx][ny] == 1:
                    visited[nx][ny] += 1
    
    return visited

air_cnt = 0
answer = 0

while air_cnt < n*m:
    answer += 1
    visited = bfs()
    
    for i in range(n):
        for j in range(m):
            if visited[i][j] > 1:
                arr[i][j] = 0
    
    cnt = 0
    for line in arr:
        cnt += line.count(0)

    air_cnt = cnt

print(answer)