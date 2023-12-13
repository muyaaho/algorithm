from heapq import heappush, heappop
import sys
input = sys.stdin.readline

q = []

for _ in range(int(input())):
    cmd = int(input())
    
    if cmd == 0:
        if q:
            x = heappop(q)
            print(-x)
        else:
            print(0)
        continue
    
    heappush(q, -cmd)