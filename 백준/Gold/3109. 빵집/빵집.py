import sys
input = sys.stdin.readline

r, c = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(r)]

dx = [-1, 0, 1]
dy = [-1, -1, -1]

answer = 0
def dfs(x, y):
    global answer
    if y == 0:
        answer += 1
        return True
    
    for i in range(3):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and arr[nx][ny] == '.':
            arr[nx][ny] = 'x'
            if dfs(nx, ny):
                return True
    
    return False

for i in range(r):
    dfs(i, c-1)
print(answer)