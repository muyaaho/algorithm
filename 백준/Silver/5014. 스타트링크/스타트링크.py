from collections import deque
import sys
input = sys.stdin.readline

f, s, g, u, d = map(int, input().split())


def bfs():
    q = deque()
    q.append(s)
    distance = [-1] * (f+1)
    distance[s] = 0

    while q:
        now = q.popleft()
        
        if now == g:
            return distance[now]
        
        for next in (now + u, now - d):
            if 0 < next <= f and distance[next] < 0:
                distance[next] = distance[now] + 1
                q.append(next)
    return "use the stairs"

print(bfs())