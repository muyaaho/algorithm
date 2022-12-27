n = int(input())
l = list(map(int,input().split()))

arr = [1]*n

for new in range(n):
    for before in range(new):
        if l[new]>l[before]:
            arr[new] = max(arr[new], arr[before]+1)

print(max(arr))