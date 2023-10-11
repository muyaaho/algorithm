import pprint
from itertools import combinations
from collections import deque
import sys
input = sys.stdin.readline


n, m = map(int, input().split())
lab_map = [list(map(int, input().split())) for _ in range(n)]

# 0 좌표 저장
# 2 좌표 저장

zeros = []
twos = []
for i in range(n):
    for j in range(m):
        if lab_map[i][j] == 0:
            zeros.append((i, j))
        elif lab_map[i][j] == 2:
            twos.append((i, j))


def spread_virus(lab):
    copy_lab = [x[:] for x in lab]
    # 2를 start로 하고 상하좌우로 움직일 수 있음
    # visited False이고 0인 곳으로
    d = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    visited = [[False]*m for _ in range(n)]
    for i, j in twos:
        q = deque()
        q.append((i, j))
        
        visited[i][j] = True
    
        # 전파시키기
        while q:
            now_x, now_y = q.popleft()
            # 4개의 방향으로 이동 가능한지 확인
            for di, dj in d:
                # 방문하지 않고, 0이고, n, m보다 크지 않다면
                go_i = now_x+di
                go_j = now_y+dj
                if 0<=go_i<n and 0<=go_j<m:
                    if not visited[go_i][go_j] and copy_lab[go_i][go_j] == 0:
                        visited[go_i][go_j] = True
                        copy_lab[go_i][go_j] = 2
                        q.append((go_i, go_j))
    cnt = 0
    
    # print('after')
    # pprint.pprint(copy_lab)            
    for line in copy_lab:
        cnt += line.count(0)
    # print(cnt)
    return cnt

com = list(combinations(zeros, 3))
# print(com)

ans = []
for xys in com:
    # print(xys)
    # 1로 바꾸기
    for x, y, in xys:
        lab_map[x][y] = 1
    
    # print('before')
    # pprint.pprint(lab_map)
    # 바이러스 전파
    ans.append(spread_virus(lab_map))
    
    # 끝날 때 다시 되돌리기
    for x, y, in xys:
        lab_map[x][y] = 0

print(max(ans))