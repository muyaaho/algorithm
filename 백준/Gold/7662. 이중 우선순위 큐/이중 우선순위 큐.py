import sys; input = sys.stdin.readline
from heapq import heappush, heappop

def max_sync():
    while maxq and not visited[maxq[0][1]]:
        heappop(maxq)

def min_sync():
    while minq and not visited[minq[0][1]]:
        heappop(minq)


for _ in range(int(input())):
    
    minq, maxq = [], []
    visited = [False] * 1_000_001
    for i in range(int(input())):
        
        cmd, n = input().rstrip().split()
        
        if cmd == 'I':
            heappush(minq, (int(n), i))
            heappush(maxq, (-int(n), i))
            visited[i] = True
        elif n == '1':
            max_sync()
            if maxq:
                visited[maxq[0][1]] = False
                heappop(maxq)
        else:
            min_sync()
            if minq:
                visited[minq[0][1]] = False
                heappop(minq)
    max_sync()
    min_sync()
    print(f'{-maxq[0][0]} {minq[0][0]}' if minq and maxq else 'EMPTY')