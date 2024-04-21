from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
indegree = [0] * (n+1)
graph = [[] for _ in range(n+1)]
for _ in range(m):
    arr = list(map(int, input().split()))
    # print(arr)
    for i in range(1, arr[0]):
        a, b = arr[i], arr[i+1]
        # print(a, b)
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