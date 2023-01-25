from collections import deque

def solution(maps):
    answer = 0
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    
    # 1일 때는 그냥 값 넣고 1이 아니라면 최솟값 집어넣기
    q = deque()
    q.append((0,0))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and maps[nx][ny] == 1:
                maps[nx][ny] += maps[x][y]
                q.append((nx, ny))
        # for x in maps:
        #     print(x)
        # print('--------------------')

    return a if (a:=maps[-1][-1]) > 1 else -1