n, k = map(int, input().split())
INF = int(1e9)
graph = [[INF] * (n+1) for _ in range(n+1)]

for a in range(1, n+1):
    graph[a][a] = 0

for _ in range(k):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for kk in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][kk] + graph[kk][b]) 

def ans():
    for i in range(1, n+1):
        for j in range(1, n+1):
            if graph[i][j] > 6:
                return "Big World!"
    return "Small World!"
print(ans())