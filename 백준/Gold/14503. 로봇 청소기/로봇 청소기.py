dm = {0:(-1, 0), 1:(0, 1), 2: (1, 0), 3:(0, -1)}

n, m = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]


answer = 0 
isBreak = False

cnt = 0
while not isBreak:
    # print(f'<{cnt}>')
    cnt += 1
    if cnt > 1000:
        break
    # 청소해야 하는 경우
    if arr[r][c] == 0:
        arr[r][c] = 2
        answer += 1
        # print(arr)
        # print()
    # 현재 칸에서 4칸 확인 해 -> 청소되지 않은 칸이 1개라도 있으면 90도 회전, 회전해서 한 칸 이동해서 청소됬느지 아닌지 확인
    # 4칸 확인 해서 청소할 수 있는지 확인
    canClean = False
    for i in range(4):
        nr = r + dm[i][0]
        nc = c + dm[i][1]
        if arr[nr][nc] == 0:
            canClean = True
            # 반시계로 방향 회전
            d = 3 if d == 0 else d-1
            # print('before if:', r + dm[d][0], c + dm[d][1], d)
            # 한 칸 이동했을 때 청소됬으면 이동(큐에 집어넣기)
            if arr[r + dm[d][0]][c + dm[d][1]] == 0:
                r = r + dm[d][0]
                c = c + dm[d][1]
                break
    if canClean:
        continue
    # 별 소득 없으면 여기서 후진하기!       
    else:
        back = (d+2)%4
        if arr[r+dm[back][0]][c + dm[back][1]] == 1:
            # 작동을 멈춘다
            isBreak = True
            continue
        else:
            r = r+dm[back][0]
            c = c + dm[back][1]
            # print('back:', r, c, d)
print(answer)