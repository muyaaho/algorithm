import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    arr = sorted([input().rstrip() for _ in range(n)])
    
    isNo = False
    for i in range(n-1):
        # print(arr[i], arr[i+1], arr[i+1].find(arr[i]))
        if arr[i+1].find(arr[i]) == 0:
            isNo = True
            break
    print('NO' if isNo else 'YES')