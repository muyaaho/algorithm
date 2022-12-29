n, m= map(int, input().split())

a = [list(map(int, input().split())) for _ in range(n)]
b = [list(map(int, input().split())) for _ in range(n)]

sum = []

for i in range(n):
    arr=[]
    for j in range(m):
        arr.append(a[i][j]+b[i][j])
    sum.append(arr)

for p in sum:
    print(*p)