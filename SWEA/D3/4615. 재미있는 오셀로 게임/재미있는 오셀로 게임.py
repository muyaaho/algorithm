dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

def setting(n):
    x = n//2-1
    axis[x][x] = 2
    axis[x][x+1] = 1
    axis[x+1][x] = 1
    axis[x+1][x+1] = 2

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    axis = [[0] * (n) for _ in range(n)]
    setting(n)
    # print(*axis, sep='\n')
    # print()

    for _ in range(m):
        a, b, color = map(int, input().split())
        a -= 1
        b -= 1
        # print('입력', a, b, color)
        axis[a][b] = color
        # print(*axis, sep='\n')
        # print()
        next = []
        for i in range(8):
            na = a + dx[i]
            nb = b + dy[i]
            wna = na
            wnb = nb

            while 0 <= wna < n and 0 <= wnb < n and axis[wna][wnb] == (3-color):
                next.append((wna, wnb))
                # print(next)
                wna += dx[i]
                wnb += dy[i]
                if 0 <= wna < n and 0 <= wnb < n and axis[wna][wnb] == color:
                    for x, y in next:
                        axis[x][y] = color
                    next = []
                    # print(*axis, sep='\n')
                    # print()
                    break
                elif not (0 <= wna < n and 0 <= wnb < n) or axis[wna][wnb] == 0:
                    next = []
                    break

    black_cnt = 0
    white_cnt = 0
    for line in axis:
        black_cnt += line.count(1)
        white_cnt += line.count(2)
    print(f"#{test_case} {black_cnt} {white_cnt}")