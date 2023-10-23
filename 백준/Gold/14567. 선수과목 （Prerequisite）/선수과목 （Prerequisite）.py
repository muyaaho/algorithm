from collections import deque
import sys
input = sys.stdin.readline


# n: 과목의 수, m: 선수 조건의 수
n, m = map(int, input().split())
indegree = [0] * (n+1)
graph = [[] for _ in range(n+1)]
answer = [0] * (n+1)

# 입력
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    # 진입차수를 1 증가
    indegree[b] += 1

# 위상 정렬 함수
def topology_sort():
    q = deque()
    
    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
            answer[i] = 1
    # 큐가 빌 때까지 반복
    while q:
        now = q.popleft()
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]:
            indegree[i] -= 1
            answer[i] = answer[now]+1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)
    # 위상 정렬을 수행한 결과 출력
    print(*answer[1:])

topology_sort()