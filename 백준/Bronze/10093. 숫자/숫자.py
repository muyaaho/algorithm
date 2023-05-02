import sys
input = sys.stdin.readline

n1, n2 = map(int, input().split())
a = min(n1, n2)
b = max(n1, n2)
if b-a-1 <= 0:
    print(0)
else:
    print(b-a-1)
print(*range(a+1, b), sep=' ')