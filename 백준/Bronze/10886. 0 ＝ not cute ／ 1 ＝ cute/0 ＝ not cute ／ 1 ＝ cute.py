arr = []
for _ in range(int(input())):
    arr.append(int(input()))

if arr.count(0) > arr.count(1):
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")