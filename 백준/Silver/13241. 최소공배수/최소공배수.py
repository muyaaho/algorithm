from math import lcm
import sys
input = sys.stdin.readline

a, b= map(int, input().split())
print(lcm(a, b))