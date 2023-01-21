from collections import deque

def solution(maps):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    
    q = deque()
    q.append((0,0))
    v = [[0]*(len(maps[0])) for _ in range(len(maps))]
    v[0][0] = 1


    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]):
                if maps[nx][ny] == 1 and not v[nx][ny]:
                    q.append((nx, ny)) 
                    maps[nx][ny] += maps[x][y] 
                    v[nx][ny] = 1
        
        
    return maps[-1][-1] if maps[-1][-1] > 1 else -1