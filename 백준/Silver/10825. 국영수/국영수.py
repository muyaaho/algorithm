from operator import itemgetter

n = int(input())
arr = []
for _ in range(n):
    name, kor, eng, math = input().split()
    arr.append((name, name.lower(), int(kor), int(eng), int(math)))

d = sorted(arr, key=itemgetter(0))
c = sorted(d, key=itemgetter(4), reverse=True)
b = sorted(c, key=itemgetter(3))
a = sorted(b, key=itemgetter(2), reverse=True)

for x in a:
    print(x[0])