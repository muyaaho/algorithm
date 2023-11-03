from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b =map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n+1)

def bfs(start):
    q = deque([start])
    visited[start] = True

    while q:
        now = q.popleft()
        for next in graph[now]:
            if not visited[next]:
                visited[next] = True
                q.append(next)

answer = 0
for i in range(1, n+1):
    if not visited[i]:
        # print(i)
        answer += 1
        bfs(i)

print(answer)