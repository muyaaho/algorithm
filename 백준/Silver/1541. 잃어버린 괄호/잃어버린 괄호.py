arr = input().split('-')
# print(arr)
arr2 = []

for x in arr:
    try:
        x = map(int, x.split('+'))
        arr2.append(sum(x))
    except:
        arr2.append(int(x))

if len(arr2) == 1:
    print(arr2[0])
else:    
    ans = arr2[0]
    for x in arr2[1:]:
        ans -= x

    print(ans)