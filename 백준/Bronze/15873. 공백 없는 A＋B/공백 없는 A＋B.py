a = input()
idx = a.find('10')
if idx == 0:
    x = int(a[:2])
    y = int(a[2:])
else:
    x = int(a[0])
    y = int(a[1:])

print(x+y)
