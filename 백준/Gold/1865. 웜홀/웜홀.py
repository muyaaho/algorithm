import sys
input = sys.stdin.readline
INF = int(1e9)

def bf():
    dist = [INF] * (n+1)

    for i in range(n):
        for s, e, t in edges:
            if dist[e] > dist[s] + t:
                dist[e] = dist[s] + t
                if i == n-1:
                    return True
    return False

for _ in range(int(input())):
    n, m, w = map(int, input().split())
    edges = []
    for _ in range(m):
        s, e, t = map(int, input().split())
        edges.append((s, e, t))
        edges.append((e, s, t))
    
    for _ in range(w):
        s, e, t = map(int, input().split())
        edges.append((s, e, -t))

    print('YES' if bf() else 'NO')