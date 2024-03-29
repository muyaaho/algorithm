'''
149p
- 연결된 부분? 0으로 이루어진 부분이 몇 개인지 찾을 때 if dfs(i, j) == Ture: result += 1
- 입력이 000111 이지만 map 함수가 실행되면서 하나씩 리스트로 들어감
- dfs는 재귀를 (x, y) 넣는 형태로 이루어짐(방문하지 않은 노드가 있다면 재귀 실행)
'''

# 연결된 묶음을 찾아주는 프로그램

n, m = map(int, input().split())    

# 2차원 리스트의 맵 정보 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x<= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] = 1
        # 상하좌우 위치도 모두 재귀적으로 호출
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

# 모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i, j) == True:
            result += 1

print(result)