n, m = map(int, input().split())
arr = [input() for _ in range(n)]

tomake = {0:'WBWBWBWB', 1:'BWBWBWBW'}
check = []
ans = []

for i in range(8):
    check.append(tomake[i%2])

for a in range(n-8+1):
    for b in range(m-8+1):
        c1 = 0
        for i, line in enumerate(arr[a:a+8]):
            for j, x in enumerate(line[b:b+8]):
                if x != check[i][j]:
                    c1 += 1

        ans.append(min(c1, 64-c1))

print(min(ans))