def checkBingo():
    cnt = 0
    db, ndb = 0, 0
    for i in range(5):
        vb, hb = 0, 0
        for j in range(5):
            # 가로 빙고인지 체크
            if carr[i][j] < 0:
                vb += 1
            # 세로 빙고인지 체크
            if carr[j][i] < 0:
                hb += 1
            # 오른쪽 아래 대각선 빙고 체크
            if i == j and carr[i][j] < 0:
                db += 1
            # 왼쪽 아래 대각선 빙고 체크
            if i+j == 4 and carr[i][j] < 0:
                ndb += 1
        if vb == 5:
            cnt += 1
        if hb == 5:
            cnt += 1
    if db == 5 :
        cnt += 1
    if ndb == 5:
        cnt += 1
    return cnt

def findAndChange(x):
    for i in range(5):
        for j in range(5):
            if carr[i][j] == x:
                carr[i][j] = -1


carr = [list(map(int, input().split())) for _ in range(5)]
mcarr = [list(map(int, input().split())) for _ in range(5)]

cnt = 1
# isBreak = False
for line in mcarr:
    for x in line:
        findAndChange(x)
        # 2개에서 4개로 될 수 있음 
        if checkBingo() >= 3:
            print(cnt)
            exit(0)
        cnt += 1