arr = list(map(int, input().split()))
l = list(range(1, 9))

if arr == l:
    print('ascending')
elif arr == l[::-1]:
    print('descending')
else:
    print('mixed')