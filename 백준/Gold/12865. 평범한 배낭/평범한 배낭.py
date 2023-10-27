import sys
input = sys.stdin.readline

n, k = map(int, input().split())
# (무게, 가치)
stuff = [list(map(int, input().split())) for _ in range(n)]
stuff = [[0,0]] + stuff

bag = [[0] * (k+1) for _ in range(n+1)]

for i in range(1, n+1):
    w, v = stuff[i]
    for j in range(1, k+1):
        if j < w:
            bag[i][j] = bag[i-1][j]
        else:
            bag[i][j] = max(v + bag[i-1][j-w], bag[i-1][j])

print(bag[i][j])