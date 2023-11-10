from collections import deque
import sys
input = sys.stdin.readline

def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = True
    
    cnt = 0
    while q:
        now = q.popleft()
        cnt += 1
        for next in graph[now]:
            if not visited[next]:
                visited[next] = True
                q.append(next)
    return cnt


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (n+1)

answer = 1
for i in range(1, n+1):
    if not visited[i]:
        answer *= bfs(i)
        answer %= 1000000007
print(answer)
    