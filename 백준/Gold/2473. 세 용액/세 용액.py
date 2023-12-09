import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

arr.sort()
mintake = sys.maxsize

for i in range(n - 2):
    start = i + 1
    end = n - 1

    while start < end:
        take = arr[i] + arr[start] + arr[end]

        if abs(take) < mintake:
            mintake = abs(take)
            result = [arr[i], arr[start], arr[end]]

        if take < 0:
            start += 1
        elif take > 0:
            end -= 1
        else:
            break
print(*result)