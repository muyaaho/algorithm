import sys
input = sys.stdin.readline
s = set()
ans = 0
for _ in range(int(input())):
    inp = input().rstrip()
    if inp == "ENTER":
        ans += len(s)
        s.clear()
    else:
        s.add(inp)
    # print(ans, s)
ans += len(s)
print(ans)