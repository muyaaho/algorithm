n = int(input())
arr = [list(input()) for _ in range(n)]

connected = [[0] * n for _ in range(n)]
for k in range(n):
    for a in range(n):
        for b in range(n):
            if a == b:
                continue
            if arr[a][b] == 'Y' or (arr[a][k] == 'Y' and arr[k][b] == 'Y'):
                connected[a][b] = 1

# print(connected)
answer = 0
for line in connected:
    answer = max(answer, sum(line))
print(answer)