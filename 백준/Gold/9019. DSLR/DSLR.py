from collections import deque
import sys
input = sys.stdin.readline

d = {0: 'D', 1: 'S', 2: 'L', 3:'R'}

def fun(x, i):
    if i == 0:
        return (x*2) % 10000
    elif i == 1:
        return (x-1) % 10000
    elif i == 2:
        return x // 1000 + (x % 1000) * 10
    else:
        return x // 10 + (x % 10) * 1000

    
for _ in range(int(input())):
    a, b = map(int, input().split())

    q = deque()
    q.append((a, ""))
    visited = [False] * 10000
    
    while q:
        x, cmd = q.popleft()
        
        if x == b:
            print(cmd)
            break
        
        for i in range(4):
            nx = fun(x, i)
            
            if not visited[nx]:
                visited[nx] = True
                q.append((nx, cmd+d[i]))