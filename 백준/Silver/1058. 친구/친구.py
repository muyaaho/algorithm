n = int(input())
arr = [list(input()) for _ in range(n)]

INF = int(1e9)
graph = [[INF] * n for _ in range(n)]

for k in range(n):
    for a in range(n):
        for b in range(n):
            if a==b:
                continue
            if arr[a][b] == 'Y' or (arr[a][k] == 'Y' and arr[k][b] == 'Y'):
                graph[a][b] = 1

answer = 0
for i in range(n):
    count = 0
    for j in range(n):
        if graph[i][j] != INF or graph[j][i] != INF:
            count += 1
    answer = max(answer, count)
print(answer)