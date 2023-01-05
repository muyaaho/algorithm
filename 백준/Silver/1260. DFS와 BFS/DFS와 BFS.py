from collections import deque
import sys
input = sys.stdin.readline

n, m, v = map(int, input().split())
edge = [list(map(int, input().split())) for _ in range(m)]
graph = [[] for _ in range(n+1)]

for start, to in sorted(edge):
    graph[start].append(to)
    graph[to].append(start)

ddd = [0]*(n+1)
bbb = [0]*(n+1)

def dfs(now):
    ddd[now] = 1
    print(now, end=' ')
    for to in sorted(graph[now]):
        if ddd[to] == 0:
            dfs(to)

def bfs(now):
    q = deque()
    q.append(now)
    bbb[now] = 1

    while q:
        n = q.popleft()
        print(n, end=' ')
        for to in sorted(graph[n]):
            if bbb[to] == 0:
                bbb[to] = 1
                q.append(to)

dfs(v)
print()
bfs(v)

