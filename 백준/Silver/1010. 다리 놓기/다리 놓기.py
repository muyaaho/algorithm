'''
조합을 문제로 나타낸 것
'''
from math import factorial

for _ in range(int(input())):
    n, m = map(int, input().split())
    a = factorial(m) // (factorial(m-n)*factorial(n))
    print(a)