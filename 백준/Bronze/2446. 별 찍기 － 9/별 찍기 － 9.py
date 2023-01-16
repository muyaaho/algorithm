a = int(input())
m = 2*a-1
for i in range(m):
    if i < a:
        print(' '*i, end='')
        print('*'*(m-i*2), end='')
        print()
    else:
        print(' '*(i-2*(i-(a-1))), end='')
        print('*'*(2*(i-(a-1))+1), end='')
        print()
