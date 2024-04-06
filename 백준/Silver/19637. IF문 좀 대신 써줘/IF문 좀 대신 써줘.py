import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dict = []
for _ in range(n):
    a, b=  input().rstrip().split()
    dict.append((int(b), a))

for _ in range(m):
    l, r = 0, len(dict) - 1
    num = int(input())
    
    while l <= r:
        mid = (l+r) // 2
        
        if num <= dict[mid][0]:
            answer = dict[mid][1]
            r = mid - 1
        else:
            l = mid + 1
    print(answer)