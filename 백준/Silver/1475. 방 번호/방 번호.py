from collections import Counter
import sys
input = sys.stdin.readline

n = input()

n = n.replace('6', '9')
c = Counter(n)
if '9' in c:
    c['9'] = c['9']//2 + c['9']%2

print(max(c.values()))