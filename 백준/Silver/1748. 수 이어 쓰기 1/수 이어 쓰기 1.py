import sys
input = sys.stdin.readline

m = {1:9, 2:90, 3:900, 4:9000, 5:90000, 6:900000, 7:9000000, 8:90000000}
one = {1:0, 2:10, 3:100, 4:1000, 5:10000, 6:100000, 7:1000000, 8:10000000, 9:100000000}
n = input().rstrip()
l = len(n)
answer = 0

for i in range(1, l):
    if i == 1:
        answer += 9
        continue
    answer += (m[i])*i

# 남은 값 더하기
answer += (int(n) - one[l]+1)*l

print(n if l == 1 else answer)