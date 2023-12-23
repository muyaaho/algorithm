from collections import deque
r, c = map(int, input().split())
arr = [list(input()) for _ in range(r)]


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[False] * c for _ in range(r)]

def bfs(i, j):
    sheep = 0
    wolf = 0
    q = deque()
    q.append((i, j))
    visited[i][j] = True
    
    while q:
        x, y = q.popleft()
        
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            
            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny]:
                # print(nx, ny)/
                if arr[nx][ny] == '#':
                    continue
                elif arr[nx][ny] == 'v':
                    wolf += 1
                elif arr[nx][ny] == 'o':
                    sheep += 1
                
                visited[nx][ny] = True
                q.append((nx, ny))
    
    return (sheep, wolf)

animals = []
for i in range(r):
    for j in range(c):
        animals.append(bfs(i, j))

answer_s, answer_w = 0, 0
for sheep, wolf in animals:
    if sheep > wolf:
        answer_s += sheep
    else:
        answer_w += wolf

print(answer_s, answer_w)