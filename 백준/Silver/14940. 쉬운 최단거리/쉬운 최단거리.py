from collections import deque
# from pprint import pprint
n, m  = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# 아래, 오, 위, 왼 (내 생각과 반대로 움직임ㅋㅋㅋ)
move = [(1, 0), (0, 1), (-1, 0), (0, -1)]

# 2찾기
break_point = False
si, sj = 0, 0
for i, line in enumerate(arr):
    if break_point:
        break
    for j, x in enumerate(line):
        if x == 2:
            si, sj = i, j
            break_point = True
            break

start = (si, sj)
visited = [[-2]*m for _ in range(n)]  

# 이동할 수 없는 곳에 있는 벽 표시
for i, line in enumerate(arr):
    for j, x in enumerate(line):
        if x == 0:
            visited[i][j] = -4

visited[si][sj] = 0
# 거기서부터 이동 시작
# i는 세로로, j는 가로로 움직임!!!
q = deque()
q.append(start)
while q:
    now_i, now_j = q.popleft()
    # print('now:',now_x, now_y)
    for to_i, to_j in move:
        di = now_i+to_i
        dj = now_j+to_j
        # print('to go:',dx, dy)
        if 0<=di<n and 0<=dj<m and visited[di][dj] == -2 and arr[di][dj] != 0:
            q.append((di, dj))
            visited[di][dj] = visited[now_i][now_j]+1
        elif 0<=di<n and 0<=dj<m and visited[di][dj] == -2 and arr[di][dj] == 0:
            visited[di][dj] = -1

# for x in visited:
#     print(x)
for line in visited:
    for x in line:
        if x == -1:
            print(0, end=' ')
        elif x == -2:
            print(-1, end=' ')
        elif x == -4:
            print(0, end=' ')
        else:
            print(x, end=' ')
        
    print()