n = int(input())
a = set(map(int, input().split()))
m = int(input())
check = list(map(int, input().split()))

for x in check:
    if x in a: print(1)
    else: print(0)