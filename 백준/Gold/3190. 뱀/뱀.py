from collections import deque
n = int(input())
k = int(input())

graph = [[0] * n for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for i in range(k):
    a, b= map(int, input().split())
    graph[a-1][b-1] = 2

l = int(input())
d = dict()
q = deque()
q.append((0, 0))

for i in range(l):
    x, c = input().split()
    d[int(x)] = c

x, y = 0, 0
graph[x][y] = 1
cnt = 0
direction = 0

def turn(alpha):
    global direction
    if alpha == 'L':
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4

while True:
    cnt += 1
    x += dx[direction]
    y += dy[direction]
    
    if not (0 <= x < n and 0 <= y < n):
        break
    
    if graph[x][y] == 2:
        graph[x][y] = 1
        q.append((x, y))
        if cnt in d:
            turn(d[cnt])
    elif graph[x][y] == 0:
        graph[x][y] = 1
        q.append((x, y))
        tx, ty = q.popleft()
        graph[tx][ty] = 0
        if cnt in d:
            turn(d[cnt])
    else:
        break

print(cnt)