from heapq import heappush, heappop
import sys
input = sys.stdin.readline

q = []
for _ in range(int(input())):
    i = int(input())
    if i == 0:
        if q:
            n, answer = heappop(q)
            print(answer)
            continue
        print(0)
        continue
    
    heappush(q, (abs(i), i))