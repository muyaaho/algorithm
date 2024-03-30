from heapq import heappush, heappop
import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
items = [0] + list(map(int, input().split()))

graph = [[] for _ in range(n+1)]
for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a].append((b, l))
    graph[b].append((a, l))

answer = 0

def bfs(start):
    q = []
    heappush(q, (0, start))
    distance = [int(1e9)] * (n+1)
    distance[start] = 0
    
    while q:
        dist, now = heappop(q)
        
        if dist > distance[now]:
            continue
        
        for next, cost in graph[now]:
            c = cost + dist
            if c < distance[next]:
                distance[next] = c
                heappush(q, (c, next))
    
    return distance
        
for i in range(1, n+1):
    arr = bfs(i)
    s = sum([items[i] for i in range(1, n+1) if arr[i] <= m])
    answer = max(answer, s)

print(answer)