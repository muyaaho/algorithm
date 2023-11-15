n, k = map(int, input().split())
arr = [True] * (n+1)

cnt = 0
answer = 0
for i in range(2, n+1):
    if arr[i]:
        for idx in range(i, n+1, i):
            if arr[idx]:
                arr[idx] = False
                cnt += 1
                if cnt == k:
                    print(idx)
                    exit(0)