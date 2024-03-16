from collections import deque
from heapq import heappush, heappop
import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# baby shark
bx, by = 0, 0
for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            bx, by = i, j
            break

target = 2
eat_count = 0
answer = 0

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(start):
    q = deque()
    q.append(start)
    visited = [[-1] * n for _ in range(n)]
    visited[start[0]][start[1]] = 0
    
    while q:
        
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < n and 0 <= ny < n) and visited[nx][ny] < 0 and arr[nx][ny] <= target:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))
    # 모든 좌표의 최소 거리 
    return visited
                
while True:
    info = dict()
    hasFish = False
    dist_map = bfs((bx, by))

    for i in range(n):
        for j in range(n):
            if eat_count < target and arr[i][j] < target and arr[i][j] > 0:
                hasFish = True
                cnt = dist_map[i][j]
                if cnt == -1:
                    continue

                if not cnt in info:
                    info[cnt] = [(i, j)]
                else:
                    heappush(info[cnt], (i, j))
    
    if not hasFish or not info:
        print(answer)
        break
    
    d1 = sorted(info.items())
    go_cnt, axis = d1[0]
    
    if len(axis) == 1:
        fx, fy = axis[0][0], axis[0][1]
    else:
        fx, fy = heappop(info[go_cnt])
    answer += go_cnt
    
    arr[fx][fy] = 9
    arr[bx][by] = 0
    bx, by = fx, fy
    
    eat_count += 1
    if eat_count == target:
        target += 1
        eat_count = 0
    