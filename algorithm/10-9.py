from collections import deque
import copy

v = int(input())
indegree = [0] * (v+1)      # 진입 차수
graph = [[] for i in range(v+1)]    # 각 노드에 연결된 간선 정보
time = [0] * (v+1)      # 각 강의 시간

for i in range(1, v+1):
    data = list(map(int, input().split()))
    time[i] = data[0]
    for x in data[1:-1]:
        indegree[i] += 1
        graph[x].append(i)

def topology_sort():
    result = copy.deepcopy(time)
    q = deque()
    
    # 처음 시작은 진입 차수가 0인 노드를 큐에 삽입
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)
    
    # 큐가 빌 때까지 반복
    while q:
        now = q.popleft()
        for i in graph[now]:
            result[i] = max(result[i], result[now]+time[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    
    for i in range(1, v+1):
        print(result[i])

topology_sort()