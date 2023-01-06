arr= sorted([int(input()) for _ in range(3)])

if arr.count(60) == 3:
    print("Equilateral")
elif sum(arr)==180 and len(set(arr))==2:
    print("Isosceles")
elif sum(arr)==180:
    print('Scalene')
else:
    print('Error')
