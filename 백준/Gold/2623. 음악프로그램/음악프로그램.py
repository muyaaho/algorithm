from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
indegree = [0] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    arr = list(map(int, input().split()))
    for i in range(1, len(arr) - 1):
        indegree[arr[i+1]] += 1
        graph[arr[i]].append(arr[i+1])

q = deque()
for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)

ans = []
while q:
    now = q.popleft()
    ans.append(now)
    
    for next in graph[now]:
        indegree[next] -= 1
        if indegree[next] == 0:
            q.append(next)

if len(ans) == n:
    print(*ans, sep='\n')
else:
    print(0)