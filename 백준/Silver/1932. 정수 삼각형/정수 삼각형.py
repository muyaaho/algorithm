import sys
input = sys.stdin.readline

n = int(input())
tri = []
for _ in range(n):
    if n == 0:
        a = [int(input())]
    else:
        a = list(map(int, input().split()))
    tri.append(a)

for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            tri[i][j] += tri[i-1][j]
        elif j == i:
            tri[i][j] += tri[i-1][j-1]
        else:
            tri[i][j] += max(tri[i-1][j-1], tri[i-1][j])

print(max(tri[-1]))