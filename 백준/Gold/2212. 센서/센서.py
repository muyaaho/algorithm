import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
arr = sorted(map(int, input().split()))

dist = []
for i in range(n-1):
    dist.append(arr[i+1] - arr[i])

dist.sort(reverse = True)
print(sum(dist[k-1:]))