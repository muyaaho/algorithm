import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

INF = int(1e9)

graph = [[INF] * (n+1) for _ in range(n+1)]

for i in range(n+1):
    graph[i][i] = 0

for _ in range(m):
    start, end, c = map(int, input().split())
    if graph[start][end] < c:
        continue
    graph[start][end] = c

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for line in graph[1:]:
    for x in line[1:]:
        print(x if x != INF else 0, end=' ')
    print()