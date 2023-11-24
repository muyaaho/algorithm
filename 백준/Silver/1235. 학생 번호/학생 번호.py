n = int(input())
arr = [input() for _ in range(n)]

for i in range(1, len(arr[0])+1):
    s = set()
    for x in arr:
        s.add(x[::-1][:i])
    if len(s) == n:
        print(i)
        break