n = int(input())
arr = [list(map(int, input().split())) for x in range(n)]
blue, white = 0, 0


def func(ttarr):
    # 재귀 탈출
    # 다 1이면 count 추가 아니면 재귀 계속
    global blue, white
    cnt1, cnt0 = 0,0
    size = len(ttarr)
    for x in ttarr:
        if 1 not in x:
            cnt0 += 1
        elif 0 not in x:
            cnt1 += 1
    
    if cnt0 == size:
        white += 1
        return
    elif cnt1 == size:
        blue += 1
        return
    
    
    func([row[:size//2] for row in ttarr[:size//2]])
    func([row[:size//2] for row in ttarr[size//2:]])
    func([row[size//2:] for row in ttarr[:size//2]])
    func([row[size//2:] for row in ttarr[size//2:]])

func(arr)
print(white)
print(blue)