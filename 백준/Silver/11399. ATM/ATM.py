n = int(input())
arr = list(map(int, input().split()))

arr.sort()

result = arr[0]
before = arr[0]
for x in arr[1:]:
    # print(x)
    result += (before + x)
    before += x

print(result)