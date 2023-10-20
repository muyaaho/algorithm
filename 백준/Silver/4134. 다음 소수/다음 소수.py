import math
import sys
input = sys.stdin.readline

def f(n):
    for i in range(2, int(math.sqrt(n))+1):
        
        # print('n, i:',n,i)
        if n%i == 0:
            return False
    
    return True
        

for _ in range(int(input())):
    n = int(input())
    
    if n == 0 or n == 1 or n == 2:
        print(2)
        continue
    
    isPrime = False
    while not isPrime:
        
        isPrime = f(n)
        if isPrime:
            break
        n += 1
    
    print(n)