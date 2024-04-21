from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def find_i():
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 'I':
                return (i, j)
    return (-1, -1)

q = deque()
ix, iy = find_i()
q.append((ix, iy))
visited = [[False] * m for _ in range(n)]
visited[ix][iy] = True

answer = 0
while q:
    x, y = q.popleft()
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and arr[nx][ny] != 'X':
            visited[nx][ny] = True
            q.append((nx, ny))
            if arr[nx][ny] == 'P':
                answer += 1

print('TT' if answer == 0 else answer)