a ,b = map(int, input().split())

arr = []
start = 1
    
while len(arr) != b:
    for x in range(start):
        arr.append(start)
        if len(arr) == b:
            break
    start += 1

# print(arr)
print(sum(arr[a-1:b]))