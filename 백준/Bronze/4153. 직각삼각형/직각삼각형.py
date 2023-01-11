while True:
    arr=list(map(int, input().split()))
    arr.sort()
    if sum(arr) == 0:
        break
    print('right' if arr[2]**2 == arr[1]**2+arr[0]**2 else 'wrong')
