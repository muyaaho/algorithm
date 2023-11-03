from collections import deque
import sys
input =sys.stdin.readline

mv = [(1, 0, 0), (0, 0, 1), (0, 1, 0), (-1, 0, 0), (0, 0, -1), (0, -1, 0)]

INF = int(1e9)
n, m, h = map(int, input().split())
graph = []

zeroCount = 0
for i in range(h):
    arr = [list(map(int, input().split())) for _ in range(m)]
    graph.append(arr)

q = deque()

for k in range(h):
    for i in range(m):
        for j in range(n):
            if graph[k][i][j] == 0:
                zeroCount += 1
            if graph[k][i][j] == 1:
                q.append((k,i,j))

if zeroCount == 0:
    print(0)
    exit(0)

while q:
    k, i, j = q.popleft()
    for dk, di, dj in mv:
        nk = dk + k
        ni = di + i
        nj = dj + j
        if 0 <= nk < h and 0 <= ni < m and 0 <= nj <n and graph[nk][ni][nj] == 0:
            graph[nk][ni][nj] = graph[k][i][j] + 1
            q.append((nk, ni, nj))

answer = -1
for box in graph:
    for line in box:
        answer = max(answer, max(line))
        if line.count(0)>0:
            print(-1)
            exit(0)
# print(graph)/
print(answer-1)