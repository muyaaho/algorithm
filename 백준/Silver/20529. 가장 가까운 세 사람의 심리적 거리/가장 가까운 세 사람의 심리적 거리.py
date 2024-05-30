from itertools import combinations
import sys
input = sys.stdin.readline

def dist(com):
    result = 0
    a, b, c = com
    
    for i in range(4):
        if a[i] != b[i]:
            result += 1
        if b[i] != c[i]:
            result += 1
        if a[i] != c[i]:
            result += 1
    return result

for _ in range(int(input())):
    answer = sys.maxsize
    n = int(input())
    arr = list(input().rstrip().split())
    
    if n > 32:
        print(0)
    else:
        for com in combinations(arr, 3):
            answer = min(answer, dist(com))
        print(answer)