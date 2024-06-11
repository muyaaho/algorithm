import sys
input = sys.stdin.readline

def cal(arr):
    m, n, x, y = arr
    k = x
    while k <= m * n:
        if (k-x) % m == 0 and (k-y) % n == 0:
            return k
        k += m
    return -1

for _ in range(int(input())):
    print(cal(map(int, input().split())))