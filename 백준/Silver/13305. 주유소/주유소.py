import sys
input = sys.stdin.readline

n = int(input())
length = list(map(int, input().split()))
cost = list(map(int, input().split()))


prev = cost[0]
answer = length[0]*prev
for i in range(1, n-1):
    now = cost[i]
    if now < prev:
        answer += length[i]*now
        prev = now
    else:
        answer += length[i]*prev

print(answer)