import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
x = int(input())
sarr = set(arr)

arr.sort()
answer = 0

for i in range(n):
    if arr[i] > x//2 or (x%2==0 and arr[i] == x//2):
        break
    if (x - arr[i] in sarr):
        answer += 1

print(answer)