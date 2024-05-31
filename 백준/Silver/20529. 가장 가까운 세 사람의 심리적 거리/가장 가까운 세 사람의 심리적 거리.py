from itertools import combinations
import sys
input = sys.stdin.readline


def dist(a, b, c):
    result = 0
    
    for i in range(4):
        if a[i] != b[i]:
            result += 1
        if b[i] != c[i]:
            result += 1
        if a[i] != c[i]:
            result += 1
    
    return result


for _ in range(int(input())):
    n = int(input())
    arr = list(input().rstrip().split())
    
    if n > 32:
        print(0)
    else:
        answer = sys.maxsize
        for a, b, c in combinations(arr, 3):
            answer = min(answer, dist(a, b, c))
        print(answer)