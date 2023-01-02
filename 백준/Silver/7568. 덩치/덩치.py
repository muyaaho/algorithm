n = int(input())
peoples = [list(map(int, input().split())) for _ in range(n)]
ans = []

for now in peoples:
    rank = 1
    for before in peoples:
        if now[0] < before[0] and now[1] < before[1]:
            rank += 1
    ans.append(rank)

print(*ans)

