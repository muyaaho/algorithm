n = int(input())

arr = [input().split() for _ in range(n)]

if len(arr) == 1:
    print(arr[0][0])
else:
    arr.sort(key=lambda x:(int(x[3]), int(x[2]), int(x[1]), x[0]))

    print(arr[-1][0])
    print(arr[0][0])