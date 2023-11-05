from heapq import heappush, heappop
import sys
input = sys.stdin.readline

q = []
for _ in range(int(input())):
    x = int(input())
    if x == 0:
        try:
            print(heappop(q))
        except:
            print(0)
        continue
    
    heappush(q, x)