n = int(input())
arr = list(input() for _ in range(n))

# print(arr)

for idx in range(len(arr[0])):
    diff = False
    for line_idx in range(1, n):
        if arr[0][idx] != arr[line_idx][idx]:
            diff = True
    
    if diff:
        print('?',end='')
    else:
        print(arr[0][idx], end='')