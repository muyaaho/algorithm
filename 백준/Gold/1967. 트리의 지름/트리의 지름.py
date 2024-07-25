from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))
    graph[b].append((a, cost))

def dfs(start):
    q = deque()
    q.append((start, 0))
    dist = [-1] * (n+1)
    dist[start] = 0
    
    while q:
        now, now_cost = q.popleft()
        
        for next, next_cost in graph[now]:
            if dist[next] < 0:
                dist[next] = now_cost + next_cost
                q.append((next, now_cost + next_cost))
    
    return dist.index(max(dist)), max(dist)

point, _ = dfs(1)
_, ans = dfs(point)
print(ans)