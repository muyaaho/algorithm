import sys
input = sys.stdin.readline

n = int(input())
arr = {input().rstrip() for _ in range(n)}

arr = sorted(arr)
arr = sorted(arr, key=len)

print(*arr, sep='\n')