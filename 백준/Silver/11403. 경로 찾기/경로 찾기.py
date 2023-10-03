INF = int(1e9)
n = int(input())
graph = []
for _ in range(n):
    arr = list(map(int, input().split()))
    arr2 = []
    for x in arr:
        if x == 0:
            arr2.append(INF)
        else:
            arr2.append(1)
    # print(f'arr: {arr2}')
    graph.append(arr2)


for k in range(n):
    for a in range(n):
        for b in range(n):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])


for line in graph:
    for x in line:
        if x == INF or x == 0:
            print(0, end=' ')
        else:
            print(1, end=' ')
    print()