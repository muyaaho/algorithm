import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
t, p = map(int, input().split())

answer = 0
for x in arr:
    answer += x // t
    if x % t != 0:
        answer += 1

print(answer)
print(n//p, n%p)