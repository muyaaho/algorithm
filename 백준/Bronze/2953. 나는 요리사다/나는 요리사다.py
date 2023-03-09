ans = []
for _ in range(5):
    l = list(map(int, input().split()))
    ans.append(sum(l))

m = max(ans)
print(ans.index(m)+1, m)