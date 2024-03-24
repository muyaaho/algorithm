import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
arr = sorted(map(int, input().split()))

if n <= k:
    print(0)
else:
    dist = []
    for i in range(n-1):
        dist.append(abs(arr[i] - arr[i+1]))

    dist.sort(reverse=True)
    # print(dist[(k-1):])
    print(sum(dist[(k-1):]))
