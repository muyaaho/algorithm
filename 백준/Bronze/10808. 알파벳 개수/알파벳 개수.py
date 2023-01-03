s = input()
arr = [0]*26

for x in s:
    arr[ord(x) - ord('a')] += 1
print(*arr)