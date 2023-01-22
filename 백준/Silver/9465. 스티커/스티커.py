for _ in range(int(input())):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(2)]

    for j in range(1, n):
        for i in range(2):
            if j == 1:
                arr[i][j] += arr[1-i][j-1]
            else:
                arr[i][j] += max(arr[1-i][j-1], arr[1-i][j-2])

    print(max(arr[0][-1], arr[1][-1]))