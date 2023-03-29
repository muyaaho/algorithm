import sys
input = sys.stdin.readline

m = [25, 10, 5, 1]
for _ in range(int(input())):
    c = int(input())   
    for x in m:
        print(c//x, end=' ')
        c %= x
    print()