import sys
input = sys.stdin.readline

ans = set()
for _ in range(int(input())):
    arr = list(map(int, input().split()))
    if arr.count(arr[0]) == 3:
        ans.add(10000 + arr[0]*1000)
    elif arr.count(arr[0]) == 2:
        ans.add(1000 + arr[0] * 100)
    elif arr.count(arr[1]) == 2:
        ans.add(1000 + arr[1] * 100)
    else:
        ans.add(max(arr) * 100)

print(max(ans))