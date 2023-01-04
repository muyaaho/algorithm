n = int(input())
l = list(map(int, input().split()))

print(len([x for x in l if x%10==n]))