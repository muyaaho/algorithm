from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def bfs(i, j):
    q.append((i, j))
    visited[i][j] = True
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < n and 0 <= ny < m and (not visited[nx][ny]) and graph[nx][ny] == 1:
                visited[nx][ny] = True
                q.append((nx, ny))
                


for _ in range(int(input())): 
    m, n, k = map(int, input().split())
    graph = [[0]*m for _ in range(n)]
    
    for _ in range(k):
        a, b = map(int, input().split())
        graph[b][a] = 1
    
    visited = [[False] * m for _ in range(n)]
    q = deque()
    
    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1 and (not visited[i][j]):
                bfs(i, j)
                cnt += 1
    print(cnt)