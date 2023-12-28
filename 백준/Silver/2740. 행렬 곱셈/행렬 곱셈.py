n, m = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]

_, k = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(m)]

for a in range(n):
    for b in range(k):
        value = 0
        for c in range(m):
            value += A[a][c] * B[c][b]
        print(value, end=' ')
    print()