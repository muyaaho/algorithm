"""
시간이 주어졌는데,, 이건 그냥 더하면 되는 건가? 아니면 각 인덱스에 시간 넣기?
time 이라는 리스트를 만들어야 할지...

"""
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
# print(indegree)
# print(graph)
# print(time)
q = deque()

for i in range(1, n + 1):
    if indegree[i] == 0:
        q.append(i)

answer = [0] * (n + 1)
while q:
    now = q.popleft()

    answer[now] += time[now]
    # print("now:", now)
    # print("answer[now]:", answer[now])

    for next in graph[now]:
        indegree[next] -= 1
        answer[next] = max(answer[now], answer[next])
        if indegree[next] == 0:
            
            # print(f"next: {next}, answer[{next}]: {answer[next]}")
            q.append(next)
    # print("answer:", answer)

print(*answer[1:], sep='\n')
