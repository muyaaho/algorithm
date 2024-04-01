import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
dist = [INF] * (n+1)

def bf(start):
    dist[start] = 0

    for i in range(n):
        for cur, next, cost in edges:
            if dist[cur] != INF and dist[next] > dist[cur] + cost:
                dist[next] = dist[cur] + cost
                if i == n-1:
                    return True
        
    return False

if bf(1):
    print(-1)
else:
    for x in dist[2:]:
        print(-1 if x == INF else x)