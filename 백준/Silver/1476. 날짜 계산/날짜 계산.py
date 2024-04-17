import sys
input = sys.stdin.readline

e, s, m = map(int, input().split())
i = 1

while True:
    ne = 15 if i % 15 == 0 else i % 15
    ns = 28 if i % 28 == 0 else i % 28
    nm = 19 if i % 19 == 0 else i % 19

    if ne == e and ns == s and nm == m:
        print(i)
        break
    i += 1