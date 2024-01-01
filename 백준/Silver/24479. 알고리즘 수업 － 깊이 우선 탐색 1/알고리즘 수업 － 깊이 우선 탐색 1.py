import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

n, m, r = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(n+1):
    graph[i].sort()
# print(graph)
visited = [0] * (n+1)
cnt = 0
def dfs(now):
    global cnt
    cnt += 1
    visited[now] = cnt
    # print(now, visited)
    for next in graph[now]:
        if visited[next] == 0:
            dfs(next)

dfs(r)

print(*visited[1:], sep='\n')