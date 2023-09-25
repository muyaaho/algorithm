from collections import deque

n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(int(input())):
    a, b = map(int, input().split())
    # print(a, b)
    # print(graph)
    graph[a].append(b)
    graph[b].append(a)

q = deque()
visited = [False] * (n+1)
q.append(1)
visited[1] = True

answer = 0
while q:
    now = q.popleft()
    for togo in graph[now]:
        if not visited[togo]:
            visited[togo] = True
            answer += 1
            q.append(togo)

print(answer)