from sys import stdin

a = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))

sarr = sorted(set(arr))

for i,val in enumerate(sarr):
    count = 0
    # 나중에 iterator 로 해서 next로 보거나 이런거 하셈
    for x in arr:
        if val == x:
            arr[count] = i
        count += 1

for x in arr:
    print(x, end=" ")
