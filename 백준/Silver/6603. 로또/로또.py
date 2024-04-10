from itertools import combinations
import sys
input = sys.stdin.readline

cnt = 0
while True:
    inp = list(map(int, input().rstrip().split()))
    
    if inp[0] == 0:
        break
    
    n = inp[0]
    arr = inp[1:]
    
    for c in combinations(arr, 6):
        print(*c)
    print()