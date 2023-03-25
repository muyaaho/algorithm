import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a = format(int(input()), 'b')

    for i, x in enumerate(a[::-1]):
        if x == '1':
            print(i, end=' ')
