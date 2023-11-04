from heapq import heappush, heappop
import sys
input = sys.stdin.readline

arr = []

for _ in range(int(input())):
    arr.append(tuple(map(int, input().split())))

arr.sort()

h = [0]

for start, end in arr:
    if start >= h[0]:
        heappop(h)
        heappush(h, end)
    else:
        heappush(h, end)

print(len(h))