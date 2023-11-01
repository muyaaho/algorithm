n, m = map(int, input().split())
# 각 브랜드 나옴 하나만 정해야됨

package, single = [], []

for _ in range(m):
    p,s = map(int, input().split())
    package.append(p)
    single.append(s)

pm = min(package)
sm = min(single)

answer = (n//6)*pm
answer += pm if pm < sm*(n%6) else sm*(n%6)
answer = answer if answer < sm * n else sm * n
print(answer)