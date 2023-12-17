def add_number(serial):
    s = 0
    for x in serial:
        if x.isdigit():
            s += int(x)
    return s

n = int(input())
arr = [input() for _ in range(n)]

arr.sort(key=lambda x:(len(x), add_number(x), x))
print(*arr, sep='\n')

