import sys
input = sys.stdin.readline

a = list(input().rstrip())
b = list(input().rstrip())

while len(a) < len(b):
    if b[-1] == 'A':
        b.pop()
    elif b[-1] == 'B':
        b.pop()
        b.reverse()
    else:
        break

print(1 if a == b else 0)