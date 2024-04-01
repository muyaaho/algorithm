import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

def dc(b):
    if b == 1:
        return a % c

    if b % 2 == 0:
        return ((dc(b//2) % c)**2)%c
    else:
        return ((dc(b//2) % c) ** 2 * a)%c

print(dc(b))