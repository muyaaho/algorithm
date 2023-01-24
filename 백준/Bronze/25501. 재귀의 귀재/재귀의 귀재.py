n = int(input())
def recurison(str, l, r, cnt):
    cnt += 1
    if l>=r: 
        return [1, cnt]
    elif str[l] != str[r]: 
        return [0, cnt]
    else: 
        return recurison(str, l+1, r-1, cnt)

def isPalindrome(str):
    return recurison(str, 0, len(str)-1, 0)

for _ in range(n):
    print(*isPalindrome(input()))