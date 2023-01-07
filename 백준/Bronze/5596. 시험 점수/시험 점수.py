a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(sum(a) if sum(a)>=sum(b) else sum(b))