n = int(input())
l = list(map(int, input().split()))

d = {num:ind for ind, num in enumerate(sorted(set(l)))}
answer = [d[x] for x in l]
print(*answer)