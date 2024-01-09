from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
time = [0] * (n + 1)
for i in range(1, n + 1):
    # 건물을 짓는데 걸리는 시간, 그 건물을 짓기 위해 먼저 지어져야 하는 건물의 번호
    arr = list(map(int, input().split()))
    time[i] = arr[0]
    for x in arr[1:]:
        if x == -1:
            break
        graph[x].append(i)
        indegree[i] += 1
q = deque()

for i in range(1, n + 1):
    if indegree[i] == 0:
        q.append(i)

answer = [0] * (n + 1)
while q:
    now = q.popleft()
    answer[now] += time[now]

    for next in graph[now]:
        indegree[next] -= 1
        answer[next] = max(answer[now], answer[next])
        if indegree[next] == 0:
            q.append(next)

print(*answer[1:], sep="\n")