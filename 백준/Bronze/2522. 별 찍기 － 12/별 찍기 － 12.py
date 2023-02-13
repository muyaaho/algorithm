import sys
input = sys.stdin.readline

n = int(input())

for x in range(1, 2*n):
    if x > n:
        print(' '*(x-n), end='')
        print('*'*(2*n-x))
    else:
        print(' '*(n-x), end='')
        print('*'*x)
