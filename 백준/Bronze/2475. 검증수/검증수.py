arr = list(map(int, input().split()))

print(sum([x*x for x in arr])%10)