a = int(input())

def f(n):
    if n==1 or n == 0:
        return 1
    else:
        return n*f(n-1)

print(f(a))