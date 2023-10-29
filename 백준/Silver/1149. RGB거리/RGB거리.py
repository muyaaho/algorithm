n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    for j in range(3):
        if j == 0:
            arr[i][j] = min(arr[i][j] + arr[i-1][j+1], arr[i][j] + arr[i-1][j+2])
        elif j == 1:
            arr[i][j] = min(arr[i][j] + arr[i-1][j-1], arr[i][j] + arr[i-1][j+1])
        else:
            arr[i][j] = min(arr[i][j] + arr[i-1][j-2], arr[i][j] + arr[i-1][j-1])
print(min(arr[-1]))