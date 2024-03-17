from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

start, end = map(int, input().split())

# 옮길 수 있는 mid 중량을 가지고 start에서 end로 이동할 수 있는지
def start_to_end(mid):
    q = deque([start])
    visited = [False] * (n+1)
    visited[start] = True
    
    while q:
        now = q.popleft()
        if now == end:
            return True
        
        for next, cost in graph[now]:
            if not visited[next] and mid <= cost:
                q.append(next)
                visited[next] = True

left, right = 1, 1_000_000_000
answer = 0

while left <= right:
    mid = (left + right) // 2
    
    if start_to_end(mid):
        answer = max(answer, mid)
        left = mid + 1
    else:
        right = mid - 1

print(answer)