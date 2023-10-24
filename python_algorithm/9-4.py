# 플로이드 워셜 알고리즘(n이 100이하로 매우 한정적임. 이걸 사용하면 빠르게 풀기 가능)
# 모든 구간의 답을 구하고 정답인 부분 뽑아내기
INF = int(1e9)

# 노드의 개수 및 간선의 개수를 입력받기
n, m = map(int, input().split())
# 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n+1):
    graph[a][a] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
# 연결되면 양방향으로 1만큼 이동
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 거쳐 갈 노드 X와 최종 목적지 노드 K를 입력받기
x, k = map()

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과를 출력
distance = graph[1][k] + graph[k][x]

# 도달할 수 없는 경우, -1을 출력
if distance >= INF:
    print(-1)
# 도달할 수 있다면, 최단 거리를 출력
else:
    print(distance)