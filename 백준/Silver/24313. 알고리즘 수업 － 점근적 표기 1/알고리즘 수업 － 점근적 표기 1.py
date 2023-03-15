a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

for i in range(n0, 101):
    if a1*i + a0 > c*i:
        print(0)
        break
    else:
        continue
if i == 100:
    print(1)
