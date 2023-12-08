from heapq import heappush, heappop

h = []
n = int(input())

for _ in range(n):
    numbers = map(int, input().split())
    for num in numbers:
        if len(h) < n:
            heappush(h, num)
        else:
            if h[0] < num:
                heappop(h)
                heappush(h, num)
print(h[0])