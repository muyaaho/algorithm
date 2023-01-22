from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    
    q = deque()
    q.append((0, 0))
    v = [[False]*m for i in range(n)]
    v[0][0] = True
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <n and 0<= ny < m and not v[nx][ny] and maps[nx][ny] == 1:
                q.append((nx, ny))
                v[nx][ny] = True
                maps[nx][ny] += maps[x][y]
    
    return maps[-1][-1] if maps[-1][-1]> 1 else -1