from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]

q = deque()
q.append((0,0))

d = [(1, 0), (0, 1), (-1, 0), (0, -1)]

while q:
    i, j = q.popleft()
    for di, dj in d:
        ni = di+i
        nj = dj+j
        if 0<= ni < n and 0 <= nj < m and arr[ni][nj] == 1:
            arr[ni][nj] = arr[i][j] + 1
            q.append((ni, nj))
            
print(arr[n-1][m-1])