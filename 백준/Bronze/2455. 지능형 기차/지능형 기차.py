max, p = 0, 0
for _ in range(4):
    i, o = map(int, input().split())
    p += o
    p -= i

    if max < p:
        max = p

print(max)