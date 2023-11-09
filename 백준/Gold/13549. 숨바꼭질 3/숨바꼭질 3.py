from heapq import heappush, heappop
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

q = []
heappush(q, (0, n))
distance = [int(1e9)] * (2*max(n, k)+1)
distance[n] = 0
# 동생이 만약 수빈보다 전에 있다면?
while q:
    time, now = heappop(q)
    if 0 <= 2*now <= k*2:
        if time < distance[now*2]:
            distance[now*2] = time
            heappush(q, (time, now*2))
            # continue
    if now+1 <= k*2:
        if time + 1 < distance[now+1]:
            distance[now+1] = time+1
            heappush(q, (time+1, now+1))
    if now-1 >= 0:
        if time + 1 < distance[now-1]:
            distance[now-1] = time + 1
            heappush(q, (time+1, now-1))
    
# print(distance)
print(distance[k])