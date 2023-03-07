n = int(input())
for i in range(n):
    print(' '*(n-i-1), end='')
    for j in range(2*i + 1):
        if j % 2 == 0:
            print("*", end='')
        else:
            print(' ', end='')
    print()