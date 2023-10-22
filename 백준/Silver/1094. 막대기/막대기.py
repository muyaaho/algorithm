from heapq import heappush, heappop

x = int(input())
arr = []

heappush(arr, 64)

while sum(arr) != x:
    a = heappop(arr)
    heappush(arr, a//2)
    if sum(arr) < x:
        heappush(arr, a//2)
print(len(arr))
