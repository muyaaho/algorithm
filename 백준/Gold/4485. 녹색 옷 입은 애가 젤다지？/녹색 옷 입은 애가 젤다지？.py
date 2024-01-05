from heapq import heappush, heappop
import sys

input = sys.stdin.readline
INF = int(1e9)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dijkstra(n):
    q = []
    heappush(q, (arr[0][0], 0, 0))

    while q:
        dist, x, y = heappop(q)

        if dist > visited[x][y]:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                cost = dist + arr[nx][ny]
                if cost < visited[nx][ny]:
                    visited[nx][ny] = cost
                    heappush(q, (cost, nx, ny))


cnt = 0
while True:
    cnt += 1
    n = int(input())
    if n == 0:
        break

    arr = [list(map(int, input().split())) for _ in range(n)]

    visited = [[INF] * n for _ in range(n)]
    visited[0][0] = arr[0][0]
    dijkstra(n)
    print(f"Problem {cnt}: {visited[n-1][n-1]}")
