n = int(input())
arr = sorted(map(int, input().split()), reverse=True)

answer = 0
for i in range(n):
    answer = max(arr[i] + 1 + i, answer)

print(answer+1)