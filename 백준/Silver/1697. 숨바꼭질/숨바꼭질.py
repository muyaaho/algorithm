from collections import deque

n, k = map(int, input().split())

q = deque()
q.append(n)
visited = [int(1e9)]* 100_001
visited[n] = 0

d = [1, -1, 2]

# 시간을 visited에 어떻게 녹여낼 것인가..?
while q:
    x = q.popleft()
    
    for i in d:
        if i == 2:
            nx = x*2
        else:
            nx = x+i
        
        if 0 <= nx < 100_001:
            if visited[nx] > visited[x] +1:
                q.append(nx)
                visited[nx] = visited[x] + 1

print(visited[k])