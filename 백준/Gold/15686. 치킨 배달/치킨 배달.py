from itertools import combinations
n, m = map(int, input().split())
arr = []

house,chicken = [], []
for i in range(n):
    line = list(map(int, input().split()))  
    for j in range(n):
        if line[j] == 1:
            house.append((i, j))
        elif line[j] == 2:
            chicken.append((i, j))

answer = 1e9
for m_chickens in combinations(chicken, m):
    chi_len = 0
    for hx, hy in house:    # 집마다 
        min_chi = 1e9
        for cx, cy in m_chickens:   # 가장 최소의 치킨 거리를 구해
            min_chi = min(min_chi, abs(hx - cx) + abs(hy - cy))
        chi_len += min_chi
    answer = min(answer, chi_len)
print(answer)