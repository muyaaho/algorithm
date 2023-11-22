from collections import Counter
r, c, k = map(int, input().split())

arr = [[0] * 100 for _ in range(100)]

for i in range(3):
    x, y, z = map(int, input().split())
    arr[i][0] = x
    arr[i][1] = y
    arr[i][2] = z

def get_sort(cut_line):
    counter = [(i, j) for i, j in Counter(cut_line).items() if i > 0]
    counter.sort(key=lambda x: (x[1],x[0]))
    return counter

def print_arr(rlen, clen):
    for line in arr[:rlen]:
        print(line[:clen])

def r_cal(rlen, clen):
    col_result = 0
    for i, line in enumerate(arr[:rlen]):
        cut_line = line[:rlen]
        counter = get_sort(cut_line)
        now_col = len(counter) * 2
        for j, (x, cnt) in enumerate(counter):
            arr[i][j*2] = x
            arr[i][j*2 + 1] = cnt
        if now_col < clen:
            for j in range(now_col, clen):
                arr[i][j] = 0
        col_result = max(col_result, now_col)

    
    return col_result

def l_cal(rlen, clen):
    row_result = 0

    for j in range(clen):
        cut_line = list(zip(*arr))[j]
        counter = get_sort(cut_line[:rlen])
        now_row = len(counter) * 2
        for i, (x, cnt) in enumerate(counter):
            arr[i*2][j] = x
            arr[i*2+1][j] = cnt
        if now_row < rlen:
            for i in range(now_row, rlen):
                arr[i][j] = 0
        row_result = max(row_result, now_row)
    return row_result



def solution(rlen, clen):
    time = 0
    while arr[r-1][c-1] != k:
        time += 1
        if time > 100:
            return -1
        if rlen >= clen:
            clen = r_cal(rlen, clen)
        else:
            rlen = l_cal(rlen, clen)
    return time
print(solution(3,3))