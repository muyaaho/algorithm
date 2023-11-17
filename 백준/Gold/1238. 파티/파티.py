from heapq import heappush, heappop
import sys
input = sys.stdin.readline
INF = int(1e9)

def dij(start, fin):
    # end점에 가면 종료
    q = []
    heappush(q, (0, start))
    distance = [INF] * (n+1)
    
    while q:
        dist, now = heappop(q)
        if distance[now] < dist:
            continue
        for cost, end in graph[now]:
            c = cost + dist
            if c < distance[end]: 
                
                distance[end] = c
                heappush(q, (c, end))
    return distance[fin]


n, m, x = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    start, end, cost= map(int, input().split())
    graph[start].append((cost, end))

answer= 0
for i in range(1, n+1):
    if i == x:
        continue
    a = dij(i, x)
    b = dij(x, i)
    answer = max(answer, a+b)

print(answer)