n = int(input())

for x in range(n):
    print(' '*x, end = '')
    print('*'*((n-x)*2-1))