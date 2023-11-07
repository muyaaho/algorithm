from itertools import combinations
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

house, chicken = [], []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            house.append((i, j))
        elif arr[i][j] == 2:
            chicken.append((i, j))

choosechi = combinations(chicken, m)
answer = 1e9
for x in choosechi:
    city_chi = 0
    for hx, hy in house:
        min_chi = 999999
        for axis in x:
            min_chi = min(min_chi, abs(hx-axis[0])+abs(hy-axis[1]))
        city_chi += min_chi
    answer = min(answer, city_chi)
print(answer)