from heapq import heappush, heappop
import sys
input = sys.stdin.readline

n = int(input())
h = []
for _ in range(n):
    numbers = list(map(int, input().split()))
    
    for num in numbers:
        if len(h) < n:
            heappush(h, num)
        else:
            if h[0] < num:
                heappop(h)
                heappush(h, num)
print(h[0])