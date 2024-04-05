import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dict = {}

for _ in range(n):
    id, pw = input().rstrip().split()
    dict[id] = pw

for _ in range(m):
    find_id = input().rstrip()
    print(dict[find_id])