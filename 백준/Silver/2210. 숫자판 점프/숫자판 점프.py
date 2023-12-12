import sys
input = sys.stdin.readline

arr = [list(input().split()) for _ in range(5)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

s = set()

def dfs(cnt, m, x, y):
    if cnt == 6:
        s.add(m)
        return
    
    for i in range(4):
        nx = x + dx[i]  
        ny = y + dy[i]
        
        if 0 <= nx < 5 and 0 <= ny < 5:
            dfs(cnt + 1, m + arr[nx][ny], nx, ny)

for i in range(5):
    for j in range(5):
        dfs(0, "", i, j)

print(len(s))