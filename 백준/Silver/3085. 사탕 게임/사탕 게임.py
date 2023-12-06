import sys
input = sys.stdin.readline

n = int(input())
arr = [list(input().rstrip()) for _ in range(n)]
answer = 0

def check():
    global answer
    for i in range(n):
        cnt = 1
        for j in range(1, n):
            if arr[i][j] == arr[i][j-1]:
                cnt += 1
                answer = max(cnt, answer)
            else:
                cnt = 1
        cnt = 1
        for j in range(1, n):
            if arr[j][i] == arr[j-1][i]:
                cnt += 1
                answer = max(cnt, answer)
            else:
                cnt = 1

for i in range(n):
    for j in range(n):
        if j + 1 < n:
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
            check()
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
        if i + 1  < n:
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
            check()
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]

print(answer)