from heapq import heappush, heappop
import sys
input =sys.stdin.readline

n, k = map(int, input().split())
gems = [tuple(map(int, input().split())) for _ in range(n)]
bags = [int(input()) for _ in range(k)]

gems.sort()
bags.sort()

tmp = []
answer = 0
for bag in bags:
    while gems and gems[0][0] <= bag:
        heappush(tmp, -gems[0][1])
        heappop(gems)
    if tmp:
        answer -= tmp[0]
        heappop(tmp)
print(answer)