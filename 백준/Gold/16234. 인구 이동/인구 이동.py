from collections import deque
import sys
input = sys.stdin.readline

n, l, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
count = 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 좌표를 구함
def bfs(startx, starty):
    s = set()
    q = deque([(startx, starty)])
    
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            
            if 0 <= nx < n and 0 <= ny < n:
                if l <= abs(arr[x][y] - arr[nx][ny]) <= r and not visited[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = True
                    visited[x][y] = True
                    s.add((nx, ny))
                    s.add((x, y))
    
    return s

is_end = True
while True:
    visited = [[False] * n for _ in range(n)]
    set_list = []
    # print(count)
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                s = bfs(i, j)
                if s:
                    set_list.append(s)

    
    if set_list:
        for s in set_list:
            avg_sum = sum([arr[x][y] for x, y in s])
            # print(avg_sum)
            avg = avg_sum // len(s)
            # print(len(s))
            for i, j in s:
                arr[i][j] = avg
    else:
        break

    count += 1

print(count)