'''
152p
- 시작 위치가 정해져 있음(모든 좌표에서 시작하지 않아도 됨)
- 그래프 자체에 값을 넣어버림(graph[x][y] = result)
- 구현 문제 처럼 dx, dy가 있어서 4방향으로 이동
- min을 쓰지 않아도 되는게, popleft된 값 + 1이 되는 거라서 1 2 이런 식으로 퍼지게 됨!
                                                  2 2
- 구해서 마지막 좌표 값을 출력하면 됨
- 입력이 000001111 이런 식일 때 split()을 하지 않아도 리스트로 입력됨! map을 하면서 하나씩 int로 바꾸기 때문에 하나씩 리스트로 들어가는 것 같음
    graph = []
    for i in range(3):
        graph.append(list(map(int, input())))
    (입력)
    123
    123
    123
    (결과)
    >>>[[1, 2, 3], [1, 2, 3], [1, 2, 3]]
- visited가 없어도 되는 이유: 그래프 값 자체를 바꾸기 때문에 1이면 방문하지 않은 노드!
'''

from collections import deque

n, m = map(int, input().split())
# 2차원 리스트의 맵 정보 받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))
    
# 이동할 네 방향 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 소스코드 구현
def bfs(x, y):
    queue = deque()
    queue.append(x, y)
    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 네 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록 하고 큐에 넣기
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n-1][m-1]

print(bfs(0,0))