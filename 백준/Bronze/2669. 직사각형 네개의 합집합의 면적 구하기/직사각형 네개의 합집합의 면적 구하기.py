arr = [[0] * 100 for _ in range(100)]

for _ in range(4):
    a,b,c,d = map(int, input().split())
    for i in range(a, c):
        for j in range(b, d):
            arr[i][j] = 1

print(sum([x.count(1) for x in arr]))