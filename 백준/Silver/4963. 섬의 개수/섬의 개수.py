from collections import deque

def bfs(x, y) :
    q = deque()
    q.append((x, y))
    maps[x][y] += 1
    
    while q:
        nx, ny = q.popleft()
        for i in range(8):
            gx = nx + dx[i]
            gy = ny + dy[i]
            
            if 0<= gx < b and 0 <= gy < a and maps[gx][gy] == 1:
                q.append((gx, gy))
                maps[gx][gy] +=1 
        

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    
    maps = [list(map(int, input().split())) for _ in range(b)]

    answer = 0
    for i in range(b):
        for j in range(a):
            if maps[i][j] == 1:
                bfs(i, j)
                answer += 1
    
    print(answer)