from heapq import heappush, heappop

# 가로, 세로
m, n = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

distance = [[-1] * m for _ in range(n)]
def dijkstra():
    q = []
    heappush(q, (0, 0, 0))
    
    
    while q:
        cost, x, y = heappop(q)
        
        if cost < distance[x][y]:
            continue
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and distance[nx][ny] == -1:
                c = cost + arr[nx][ny]
                distance[nx][ny] = c
                heappush(q, (c, nx, ny))
dijkstra()
print(0 if distance[n-1][m-1] < 0 else distance[n-1][m-1])