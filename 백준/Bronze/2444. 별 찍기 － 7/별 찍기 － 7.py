n = int(input())

for x in range(1, 2*n):
    if x>n:
        x = x-2*(x-n)
    print(' '*(n-x), end = '')
    print('*'*(2*x-1))