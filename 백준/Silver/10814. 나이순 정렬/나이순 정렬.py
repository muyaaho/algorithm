import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    a, b = input().rstrip().split(' ')
    arr.append((int(a),b))

for a, b in sorted(arr, key = lambda x: x[0]):
    print(a, b)