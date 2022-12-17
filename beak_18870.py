from sys import stdin

a = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))

sarr = sorted(set(arr))
dict=dict(enumerate(sarr))
print(dict)

for x in arr:
    print(dict.get(x), end='')