s = [int(input()) for X in range(4)]
k = [int(input()) for x in range(2)]

print(sum(sorted(s)[1:], max(k)))