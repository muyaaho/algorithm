for i in range(int(input())):
    arr = list(map(int, input().split()))
    arr = sorted(arr[1:])
    
    print('Class',i+1)
    
    max_gap = 0
    for idx in range(len(arr)-1):
        gap = arr[idx+1]-arr[idx]
        if max_gap < gap:
            max_gap = gap
    print(f'Max {arr[-1]}, Min {arr[0]}, Largest gap {max_gap}')