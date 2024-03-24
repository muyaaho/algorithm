from collections import deque
import sys
input = sys.stdin.readline

n, l, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(startx, starty):
    s = set()
    q = deque([(startx, starty)])
    
    visited[startx][starty] = True
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if l <= abs(arr[x][y] - arr[nx][ny]) <= r:
                    q.append((nx, ny))
                    s.add((nx, ny))
                    s.add((x, y))
                    visited[nx][ny] = True
    return s

answer = 0
while True:
    set_list = []
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                if s:=bfs(i, j):
                    set_list.append(s)
    
    if set_list:
        answer += 1
        for s in set_list:
            avg = sum([arr[x][y] for x, y in s]) // len(s)
            for x, y in s:
                arr[x][y] = avg
    else:
        break

print(answer)