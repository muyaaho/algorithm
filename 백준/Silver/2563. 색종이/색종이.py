n = int(input())

coord = [list(map(int, input().split())) for _ in range(n)]
area = [[0 for _ in range(101)] for _ in range(101)]

for x, y in coord:
    for i in range(x, x+10):
        for j in range(y, y+10):
            area[i][j] = 1

answer = 0
for line in area:
    answer += line.count(1)

print(answer)
