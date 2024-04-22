from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)
for _ in range(m):
    arr = list(map(int, input().split()))
    k = arr[0]
    for i in range(1, k):
        a, b = arr[i], arr[i+1]
        graph[a].append(b)
        indegree[b] += 1

q = deque()
for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)

answer = []
while q:
    now = q.popleft()
    answer.append(now)
    
    for next in graph[now]:
        indegree[next] -= 1
        if indegree[next] == 0:
            q.append(next)

if len(answer) == n:
    print(*answer, sep='\n')
else:
    print(0)