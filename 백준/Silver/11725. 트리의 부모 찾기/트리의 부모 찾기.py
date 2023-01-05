import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    start, to = map(int, input().split())
    graph[start].append(to)
    graph[to].append(start)

q = deque()
visit = [0]*(n+1)
q.append(1)
visit[1] = 1

while q:
    now = q.popleft()
    for to in graph[now]:
        if visit[to] == 0:
            visit[to] = now
            q.append(to)

for x in visit[2:]:
    print(x)
