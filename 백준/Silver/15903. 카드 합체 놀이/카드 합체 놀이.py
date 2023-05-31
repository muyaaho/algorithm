from heapq import heappush, heappop, heapify
import sys
input = sys.stdin.readline


n, m = map(int, input().split())
arr = list(map(int, input().split()))

heapify(arr)
# print(arr)
for _ in range(m):
    a = heappop(arr) + heappop(arr)
    heappush(arr, a)
    heappush(arr, a)

print(sum(arr))