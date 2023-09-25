from collections import deque
# from pprint import pprint

n = int(input())

graph = []

for _ in range(n):
    graph.append(list(input()))

to_view = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def bfs(x, y):
    q.append((x, y))
    visited[x][y] = True
    
    while q:
        now_x, now_y = q.popleft()
        now_color = graph[now_x][now_y]
        for to_x, to_y in to_view:
            new_x = now_x+to_x
            new_y = now_y+to_y
            if (0 <= new_x < n and 0 <= new_y < n) and not visited[new_x][new_y]:
                new_color = graph[new_x][new_y]
                if new_color == now_color:
                    q.append((new_x, new_y))
                    visited[new_x][new_y] = True
    
    # print(x, y)
    # pprint(visited)

q = deque()
cnt  = 0
visited = [[False]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            cnt += 1
            # print(f'i: {i}, j: {j}, cnt: {cnt}')
            # print()


for i in range(n):
    for j in range(n):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'


cnt_gr = 0
visited = [[False]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            cnt_gr += 1
            
print(cnt, cnt_gr)