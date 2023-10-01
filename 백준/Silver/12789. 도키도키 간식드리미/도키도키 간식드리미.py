n = int(input())

arr = list(map(int, input().split()))
cnt = 1
stack = []
now = arr[:]
fin = []

# 하나씩 반복문을 진행해야 됨 cnt가 어디에 있는지에 따라!
while cnt != n:
    
    # cnt가 arr[0]에 있는지(오른쪽)
    if arr and cnt == arr[0]:
        cnt += 1
        arr.pop(0)
    # cnt가 stack에 있는지(아래)
    elif stack and cnt == stack[-1]:
        cnt += 1
        stack.pop()
    # cnt가 아무데도 없는지 -> stack에 집어넣는다. 만약 집어넣을게 없다면 sad
    else:
        if arr:
            stack.append(arr[0])
            arr.pop(0)
        else:
            print('Sad')
            exit(0)
print('Nice')
