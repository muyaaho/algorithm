# 1에서 출발하는 모든 최단 경로 구하기(다익스트라)
from heapq import heappush, heappop 
import sys

input = sys.stdin.readline
INF = int(1e9)

v, e = map(int, input().split())
start = int(input())

graph = [[] for i in range(v+1)]
distance = [INF] * (v+1)

# 모든 간선 정보 입력
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist+i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heappush(q, (cost, i[0]))

dijkstra(start)

for i, x in enumerate(distance[1:], start = 1):
    if i == start:
        print(0)
    elif x == INF:
        print('INF')
    else:
        print(x)