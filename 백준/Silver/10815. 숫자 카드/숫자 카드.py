import sys
input = sys.stdin.readline

n = int(input())
nums = set(map(int, input().split()))
m = int(input())
cards = list(map(int, input().split()))

for x in cards:
    print(1 if x in nums else 0, end=' ')