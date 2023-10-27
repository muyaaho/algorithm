import sys
input = sys.stdin.readline
n = list(input().rstrip())


def solution(n):
    if '0' not in n:
        return -1
    s = sum([int(x) for x in n])
    if s % 3 != 0:
        return -1
    n.sort(reverse=True)
    return int(''.join(n))

ans = solution(n)
print(-1 if ans < 0 else ans)