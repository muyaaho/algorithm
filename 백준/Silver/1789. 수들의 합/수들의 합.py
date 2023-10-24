import sys
input = sys.stdin.readline

s = int(input())
answer = 0
idx = 1
while answer <= s:
    # print(idx, answer)
    answer += idx
    idx += 1

print(idx-2)