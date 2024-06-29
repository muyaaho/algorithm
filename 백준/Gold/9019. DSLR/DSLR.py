from collections import deque
import sys
input = sys.stdin.readline

cmd_map = {0: 'D', 1: 'S', 2: 'L', 3: 'R'}

def cal(x, i):
    if i == 0:
        return (x*2) % 10000
    elif i == 1:
        return (x-1) % 10000
    elif i == 2:
        # 1234 -> 2341
        return (x % 1000) * 10 + x//1000
    else:
        # 1234 -> 4123
        return (x % 10) * 1000 + x//10

for _ in range(int(input())):
    a, b = map(int, input().split())
    
    q = deque()
    q.append((a, ""))
    visited = [False] * 10_001
    visited[a] = True
    
    while q:
        x, cmd = q.popleft()
        
        if x == b:
            print(cmd)
            break
        
        for i in range(4):
            nx = cal(x, i)
            
            if not visited[nx]:
                visited[nx] = True
                q.append((nx, cmd+cmd_map[i]))
    