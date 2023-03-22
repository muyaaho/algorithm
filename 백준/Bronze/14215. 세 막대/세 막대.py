arr = list(map(int, input().split()))
arr.sort()

if arr[0]+arr[1] > arr[2]:
    print(sum(arr))
else:
    c = arr[0]+arr[1]-1
    print(arr[0]+arr[1]+c)