arr = [list(map(int, input().split())) for _ in range(19)]

move = [(1, 0), (1,1), (0, 1), (-1, 1)]

for i in range(19):
    for j in range(19):
        if arr[i][j] != 0:
            stone = arr[i][j]
            # print('i, j, stone:', i, j, stone)
            # 주변에 좌표가 있는지 확인. 있다면 거기서 그 좌표로 계속 이동
            for x, y in move:
                # print('x, y:',x, y)
                for cnt in range(1, 6):
                    dx = x*cnt+i
                    dy = y*cnt+j
                    # print('dx, dy, cnt, n_stone: ', dx, dy, cnt, arr[dx][dy])
                    if not(0<=dx<19) or not(0<=dy<19) or arr[dx][dy] != stone:
                        break
                    else:
                        if cnt == 4:
                            # 다음 돌
                            if x*(cnt+1)+i<19 and y*(cnt+1)+j<19:
                                if arr[x*(cnt+1)+i][y*(cnt+1)+j] != stone:
                                # 이전 돌
                                    if i-x<0 or j-y<0 or arr[i-x][j-y] != stone:
                                    # print(arr[i-x][j-x])
                                        print(stone)
                                        print(i+1, j+1)
                                        exit()
                            else:
                                if i-x<0 or j-y<0 or arr[i-x][j-y] != stone:
                                    print(stone)
                                    print(i+1, j+1)
                                    exit()
print(0)    