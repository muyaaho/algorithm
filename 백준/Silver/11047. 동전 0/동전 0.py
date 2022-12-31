n, k = map(int, input().split())
moneys = [int(input()) for _ in range(n)]
moneys = [x for x in moneys if x<=k]
answer = 0

for m in moneys[::-1]:
    answer += k//m
    k %= m

print(answer)