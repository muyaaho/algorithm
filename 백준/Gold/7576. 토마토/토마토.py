from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 시작하기 전 모든 토마토가 익었는지 체크
def checkZero():
    for line in arr:
        if line.count(0) > 0:
            return True
    return False
    # false면 0이 1개라도 있다
    # true면 0이 1개도 없다

# 시작 좌표 보관
def findStart():
    ll = []
    for i in range(m):
        for j in range(n):
            if arr[i][j] == 1:
                ll.append((i, j))
    return ll

def bfs():
    start = findStart()
    global ans
    q = deque()
    for i in start:
        q.append(i)
        visited[i[0]][i[1]] = 0
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and arr[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                ans = visited[nx][ny]
                arr[nx][ny] = 1
                q.append((nx, ny))
    


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]
visited = [[-1] * n for _ in range(m)]
if not checkZero():
    print(0)
    exit(0)
ans = 0

bfs()
print(-1 if checkZero() else ans)
