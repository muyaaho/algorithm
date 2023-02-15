n, k = map(int, input().split())

cnt = 0
flag = True
for i in range(1, n+1):
    if n%i == 0:
        cnt += 1
    if cnt == k:
        print(i)
        flag = False
        break

if flag:
    print(0)

