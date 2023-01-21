import sys
input = sys.stdin.readline

n = int(input())
cnt = [0]*(10001)

for _ in range(n):
    x = int(input())
    cnt[x] += 1

# print('--------------')
for i in range(len(cnt)):
    for _ in range(cnt[i]):
        print(i)
