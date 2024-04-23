import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
a = input().rstrip()
b = input().rstrip()

def recu(s):

    if s == a:
        return 1
    elif len(s) == len(a):
        return 0
    
    if s[-1] == 'A':
        return recu(s[:-1])
    elif s[-1] == 'B':
        return recu(s[:-1][::-1])
    else:
        return 0

print(recu(b))