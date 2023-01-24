import sys
input = sys.stdin.readline

n = int(input())
d = {1:1, 0:2, 7:3, 6:4}

r = n%8
if 0< n <= 5:
    print(n)
        
elif r == 1 or r == 0 or r == 7 or r==6:
    print(d[r])
else:
    print(r)