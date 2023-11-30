v, e= map(int, input().split())
INF = int(1e9)

graph = [[INF] * (v+1) for _ in range(v+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a][b] = c

for k in range(1, v+1):
    for a in range(1, v+1):
        for b in range(1, v+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

answer = INF
for i in range(1, v+1):
    answer = min(answer, graph[i][i])
print(-1 if answer >= INF else answer)