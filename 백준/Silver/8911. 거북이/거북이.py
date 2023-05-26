go = {0:(0,1), 1:(1,0), 2:(0, -1), 3:(-1, 0)}
for _ in range(int(input())):
    # 초기 세팅
    coord = set()
    coord.add((0,0))
    
    idx = 0
    now = [0, 0]
    
    # 명령어 받아서 좌표 coord에 넣기
    for x in input():
        if x == 'F':
            now[0] += go[idx][0]
            now[1] += go[idx][1]
            coord.add(tuple(now))
            
        elif x == 'B':
            k = idx
            idx = (idx+2)%4
            now[0] += go[idx][0]
            now[1] += go[idx][1]
            idx = k
            coord.add(tuple(now))

        elif x == 'L':
            # ((idx-1)+4)%4
            idx = (idx+3)%4
        
        elif x == 'R':
            idx = (idx+1)%4
        
        else:
            print('잘못된 입력입니다.')
        # print(x, idx, now)
    # 직사각형의 넓이
    # print(coord)
    xs = [a[0] for a in coord]
    ys = [a[1] for a in coord]
    
    xmin = min(xs)
    xmax = max(xs)
    ymin = min(ys)
    ymax = max(ys)
    
    print(abs((xmax-xmin)*(ymax-ymin)))