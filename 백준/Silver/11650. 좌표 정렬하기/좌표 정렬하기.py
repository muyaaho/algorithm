n = int(input())
loc = [list(map(int, input().split())) for _ in range(n)]

loc.sort()
for x in loc:
    print(*x)