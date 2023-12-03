n, l = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

for x in arr:
    if x <= l:
        l += 1
    else:
        break
print(l)