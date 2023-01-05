l = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())

a = a//c+1 if a/c-a//c > 0 else a//c
b = b//d+1 if b/d-b//d > 0 else b//d

print(l-a if a>b else l-b)