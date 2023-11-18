import sys
input = sys.stdin.readline

n, m = map(int, input().split())

INF = int(1e9)
graph = [[INF] * (n+1) for _ in range(n+1)]

for a in range(n+1):
    graph[a][a] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1

for k in range(n+1):
    for a in range(n+1):
        for b in range(n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

answer = 0
for i in range(1, n+1):
    count = 0
    for j in range(1,n+1):
        if graph[i][j] != INF or graph[j][i] != INF:
            count += 1
    if count == n:
        answer += 1

print(answer)