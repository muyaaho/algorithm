n = int(input())

for x in range(1, 2*n):
    if x > n:
        x = 2*n-x
    print('*'*(x), end='')
    print(' '*(n-x), end='')
    print(' '*(n-x), end='')
    print('*'*(x), end='')
    print()