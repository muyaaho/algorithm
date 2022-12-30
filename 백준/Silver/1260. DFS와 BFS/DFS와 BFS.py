from collections import deque

n, m, k = map(int, input().split())
graph = [[0] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

# print(graph)
vlist1 = [0]*(n+1)
vlist2 = [0]*(n+1)

def bfs(now):
    q = deque()
    q.append(now)
    vlist1[now] = 1

    while q:
        now = q.popleft()
        print(now, end=' ')
        for end in range(1, n+1):
            if vlist1[end] == 0 and graph[now][end] == 1:
                q.append(end)
                vlist1[end] = 1

def dfs(now):
    vlist2[now] = 1
    print(now, end=' ')
    for end in range(1, n+1):
        if vlist2[end] == 0 and graph[now][end] == 1:
            dfs(end)

dfs(k)
print()
bfs(k)
