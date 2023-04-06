import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dlook, dhear = set(), set()
for _ in range(n):
    dlook.add(input().rstrip())
for _ in range(m):
    dhear.add(input().rstrip())

ans = list(dlook & dhear)
print(len(ans))
print(*sorted(ans), sep='\n')