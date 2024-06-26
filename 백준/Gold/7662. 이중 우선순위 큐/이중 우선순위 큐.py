from heapq import heappush, heappop
import sys
input = sys.stdin.readline

def sync (q):
    while q and not visited[q[0][1]]:
        heappop(q)


for _ in range(int(input())):
    n = int(input())
    visited = [False] * n
    maxq, minq = [], []
    for i in range(n):
        cmd, num = input().rstrip().split()
        
        if cmd == 'I':
            heappush(minq, (int(num), i))
            heappush(maxq, (-int(num), i))
            visited[i] = True
        
        elif num == '-1':
            sync(minq)
            if minq:
                visited[minq[0][1]] = False
                heappop(minq)
        
        else:
            sync(maxq)
            if maxq:
                visited[maxq[0][1]] = False
                heappop(maxq)
        
    sync(maxq)
    sync(minq)
    
    print(f'{-maxq[0][0]} {minq[0][0]}' if maxq and minq else 'EMPTY')