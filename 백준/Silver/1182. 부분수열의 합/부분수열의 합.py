import sys
input = sys.stdin.readline


n, s = map(int, input().split())
arr = list(map(int, input().split()))


visited = [False] * n
answer = 0 
def bfs(added, idx, cnt):
    global answer
    if cnt > 0 and added == s:
        answer += 1
        # return
    
    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            bfs(added + arr[i], i+1, cnt+1)
            visited[i] = False

bfs(0, 0, 0)
print(answer)