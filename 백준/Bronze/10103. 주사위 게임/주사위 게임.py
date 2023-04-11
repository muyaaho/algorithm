a, b = 100, 100
for _ in range(int(input())):
    aa, bb = map(int, input().split())
    if aa > bb:
        b -= aa
    elif aa < bb:
        a -= bb
    else:
        continue
    
print(a)
print(b)