arr = []
for _ in range(5):
    a = input()
    arr.append(a)

for i in range(15):
    for j in range(5):
        try:
            print(arr[j][i], end='')
        except:
            continue