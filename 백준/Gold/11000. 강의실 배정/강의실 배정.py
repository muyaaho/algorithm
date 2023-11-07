from heapq import heappush, heappop
import sys
input = sys.stdin.readline

n = int(input())
graph = [tuple(map(int, input().split())) for _ in range(n)]

graph.sort()

arr = [graph[0][1]]
for s, t in graph[1:]:
    if arr[0] <= s:
        heappush(arr, t)
        heappop(arr)
    else:
        heappush(arr, t)
print(len(arr))