from collections import deque

v = int(input())
e = int(input())
network = [list(map(int, input().split())) for _ in range(e)]
network.sort()
queue = deque()
answer = []
graph = [[] for _ in range(v+1)]

for start, end in network:
    graph[start].append(end)
    graph[end].append(start)

queue.append(1)

while queue:
    now = queue.popleft()
    for end in graph[now]:
        if end not in answer:
            answer.append(end)
            queue.append(end)

print(len(answer)-1)