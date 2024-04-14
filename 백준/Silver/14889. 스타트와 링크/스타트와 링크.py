import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [False] * n

answer = sys.maxsize
def find(cnt, idx):
    global answer
    if cnt == n//2:
        start, link = 0, 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    start += arr[i][j]
                elif not visited[i] and not visited[j]:
                    link += arr[i][j]
        answer = min(answer, abs(start-link))
        return
    
    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            find(cnt + 1, i + 1)
            visited[i] = False

find(0, 0)
print(answer)