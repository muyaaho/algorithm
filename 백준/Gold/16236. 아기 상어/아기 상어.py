'''
[x] bfs 함수만들기


'''

from collections import deque
from heapq import heappush, heappop
import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# baby shark
bx, by = 0, 0
for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            bx, by = i, j
            arr[i][j] = 0
            break

target = 2
eat_count = 0
answer = 0

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 거리랑 좌표 파악, 여기는 반복문 돌려서 togo가 있을 때 실행되는 함수임
def bfs(start):
    q = deque()
    q.append(start)
    visited = [[-1] * n for _ in range(n)]
    visited[start[0]][start[1]] = 0
    
    while q:
        
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < n and 0 <= ny < n) and visited[nx][ny] < 0 and arr[nx][ny] <= target:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))
    return visited
                
    



# 고기 먹었을 때 처리는 따로 해줘야됨(값을 0으로 바꾼다거나)
# 물고기는 자신보다 작은 물고기를 먹을 수 있어서 target보다 작은 물고기를 먹어야됨
# 작은 순서대로가 아닌 작은거 아무거나 먹어도 됨

while True:
    # 반복문 돌려서 먹을 물고기 있는지 확인 
    info = dict()
    hasFish = False
    # print(f'shark:',bx, by)
    dist_map = bfs((bx, by))
    # for line in dist_map:
    #     print()
    
    for i in range(n):
        for j in range(n):
            if eat_count < target and arr[i][j] < target and arr[i][j] > 0:
                hasFish = True
                cnt = dist_map[i][j]
                if cnt == -1:
                    continue
                # dictionary에 저장
                if not cnt in info:
                    info[cnt] = [(i, j)]
                else:
                    heappush(info[cnt], (i, j))
    
    if not hasFish or not info:
        print(answer)
        break
    
    # cnt가 제일 작은 물고기 찾기
    d1 = sorted(info.items())
    # print(info)
    # print(d1)
    go_cnt, axis = d1[0]
    
    # 물고기 1개만 있으면 그 값으로 이동(count, info의 값을 저장), eat_count도 1개 줄이기
    if len(axis) == 1:
        fx, fy = axis[0][0], axis[0][1]
    # 물고기 여러마리면 정렬해서 제일 앞에 온 물고기 먹으셈(cnt == info)
    else:
        fx, fy = heappop(info[go_cnt])
    # print('go_cnt:', go_cnt)
    answer += go_cnt
    # print('fx, fy:', fx, fy)
    
    # 이동 물고기 처리
    arr[fx][fy] = 9
    # 아기상어 위치 변경
    arr[bx][by] = 0
    bx, by = fx, fy
    
    
    # 아기상어 몸 크기 업데이트
    eat_count += 1
    if eat_count == target:
        target += 1
        eat_count = 0
    # print('shark size:', target, ', eat_count:',eat_count)
    # print('answer:', answer)
    # print()
    