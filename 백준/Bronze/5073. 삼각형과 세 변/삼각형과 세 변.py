import sys
input = sys.stdin.readline

while True:
    arr = list(map(int, input().split()))
    if sum(arr) == 0:
        break
    
    arr.sort()
    if arr[0]+arr[1] <= arr[2]:
        print('Invalid')
    elif arr.count(arr[0]) == 3:
        print('Equilateral')
    elif arr.count(arr[1]) == 2:
        print('Isosceles')
    else:
        print('Scalene')
