from collections import deque
import sys
input = sys.stdin.readline

v = int(input())

graph =[[] for _ in range(v+1)]
for _ in range(v):
    arr = list(map(int, input().split()))
    n = arr[0]
    for idx in range(1, len(arr)-1, 2):
        graph[n].append((arr[idx], arr[idx+1]))

def dfs(start):
    q = deque()
    q.append((start, 0))
    distance = [-1] * (v+1)
    distance[start] = 0
    
    while q:
        now, d = q.popleft()
        
        for next, nd in graph[now]:
            if distance[next] < 0:
                distance[next] = d+nd
                q.append((next, d+nd))
    
    return distance.index(max(distance)), max(distance)

point, _ = dfs(1)
_, ans = dfs(point)
print(ans)