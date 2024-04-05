a, b, c = map(int, input().split())

def bf(b):
    if b == 1:
        return a%c
    
    if b % 2 == 0:
        return ((bf(b//2) % c) ** 2) % c
    
    return ((bf(b//2) % c) ** 2 * a) % c

print(bf(b))