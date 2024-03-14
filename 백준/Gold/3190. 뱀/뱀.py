from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

graph = [[0] * n for _ in range(n)]

for _ in range(k):
    x, y = map(int, input().split())
    graph[x-1][y-1] = 2

l = int(input())

direct_info = dict()
coords = deque()
coords.append((0, 0))

for _ in range(l):
    x, c = input().rstrip().split()
    direct_info[int(x)] = c

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
x, y = 0, 0
graph[x][y] = 1
time = 0
direction = 0

def turn(direct):
    global direction
    if direct == 'L':
        direction = (direction - 1)%4
    else:
        direction = (direction + 1)%4

while True:
    time += 1
    x += dx[direction]
    y += dy[direction]
    if not (0 <= x < n and 0 <= y < n):
        break
    
    if graph[x][y] == 2:
        coords.append((x, y))
        graph[x][y] = 1
    elif graph[x][y] == 0:
        coords.append((x, y))
        graph[x][y] = 1
        tx, ty = coords.popleft()
        graph[tx][ty] = 0
    else:
        break
    
    
    
    if time in direct_info:
        turn(direct_info[time])

print(time)