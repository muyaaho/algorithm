n, k = map(int, input().split())
l = []
answer = 0
for x in range(n):
    l.append(int(input()))

l = list(filter(lambda x : x<=k, l))

for x in l[::-1]:
    answer += k//x
    k%=x
    if k<=0:
        break

print(answer)