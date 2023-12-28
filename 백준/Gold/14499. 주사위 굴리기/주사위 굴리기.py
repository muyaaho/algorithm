n, m, x, y, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
cmds = list(map(int, input().split()))

dice = [0] * (6)
def change(cmd):
    bottom = dice[0]
    back = dice[1]
    right = dice[2]
    left = dice[3]
    forth = dice[4]
    top = dice[5]
    
    if cmd == 1:
        dice[0] = right
        dice[2] = top
        dice[3] = bottom
        dice[5] = left
    elif cmd == 2:
        dice[0] = left
        dice[2] = bottom
        dice[3] = top
        dice[5] = right
    elif cmd == 3:
        dice[0] = back
        dice[1] = top
        dice[4] = bottom
        dice[5] = forth
    elif cmd == 4:
        dice[0] = forth
        dice[1] = bottom
        dice[4] = top
        dice[5] = back

def find_axis(cmd, x, y):
    if cmd == 1 and y + 1 < m:
        y += 1
        return x, y, True
    elif cmd == 2 and y - 1 >= 0:
        y -= 1
        return x, y, True
    elif cmd == 3 and x - 1 >= 0:
        x -= 1
        return x, y, True
    elif cmd == 4 and x + 1 < n:
        x += 1
        return x, y, True
    return x, y, False

    
for cmd in cmds:
    nx, ny, can_move = find_axis(cmd, x, y)
    if not can_move:
        continue
    x, y = nx, ny
    change(cmd)
    if arr[nx][ny] == 0:
        arr[nx][ny] = dice[0]
    else:
        dice[0] = arr[nx][ny]
        arr[nx][ny] = 0
    print(dice[5])