a, b, c, m = map(int, input().split())

f = 0
result = 0
for time in range(24):
    new_f = f+a
    if new_f > m:
        f = 0 if f-c<0 else f-c
    else:
        f = new_f
        result += b

print(result)