n = int(input())

for i in range(n):
    print(' '*(n-i-1), end='')
    if i == 0:
        print('*', end='')
    elif i == n-1:
        print('*'*(2*i+1), end='')
        
    else:
        print('*', end='')
        print(' '*(2*i-1), end='')
        print('*', end='')
    print()
        