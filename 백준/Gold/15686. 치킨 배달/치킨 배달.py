from itertools import combinations
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

house = []
chicken =[]
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            house.append((i, j))
        elif arr[i][j] == 2:
            chicken.append((i, j))

ans = []
for coordinates in combinations(chicken, m):
    # 모든 집마다 치킨 m개씩 돌면서 치킨 최소인 치킨 거리 구하고 이걸 도시의 치킨거리에 더하기
    dist_chi = 0
    for hx, hy in house:
        min_chi = 9999
        for cx, cy in coordinates:
            min_chi = min(min_chi, abs(hx-cx) + abs(hy-cy))
        dist_chi += min_chi
    ans.append(dist_chi)
print(min(ans))