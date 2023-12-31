from collections import deque
n = int(input())

r1, c1, r2, c2 = map(int, input().split())

move = [(-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)]

arr = [[-1] * n for _ in range(n)]
q = deque()
q.append((r1, c1))
arr[r1][c1] = 0

while q:
    x, y = q.popleft()

    for dx, dy in move:
        nx = x + dx
        ny = y + dy
        
        if 0 <= nx < n and 0 <= ny < n:
            if arr[nx][ny] < 0:
                arr[nx][ny] = arr[x][y] + 1
                q.append((nx, ny))
            elif arr[nx][ny] > arr[x][y] + 1:
                arr[nx][ny] = arr[x][y] + 1
                q.append((nx, ny))
            
print(arr[r2][c2])