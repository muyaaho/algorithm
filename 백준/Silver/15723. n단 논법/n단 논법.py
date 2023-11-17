INF = int(1e9)
n = int(input())
graph = [[INF] * 26 for _ in range(26)]
for a in range(26):
    graph[a][a] = 0

for _ in range(n):
    inp = input()
    a, b = inp[0], inp[-1]
    aidx = ord(a) - ord('a')
    bidx = ord(b) - ord('a')
    
    graph[aidx][bidx] = 1

for k in range(26):
    for a in range(26):
        for b in range(26):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

    
m = int(input())
# 정답 바로바로 확인하면서 출력
for _ in range(m):
    inp = input()
    a, b = inp[0], inp[-1]
    aidx = ord(a) - ord('a')
    bidx = ord(b) - ord('a')
    if graph[aidx][bidx] != INF:
        print('T')
    else:
        print('F')
