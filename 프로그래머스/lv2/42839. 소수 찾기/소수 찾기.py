from itertools import permutations

n = 10000000
a = [False, False] + [True]*(n-1)
primes = set()

for i in range(2, n+1):
    if a[i]:
        primes.add(i)
        for j in range(2*i, n+1, i):
            a[j] = False

def solution(numbers):
    answer = set()
    
    for i in range(1, len(numbers)+1):
        for x in permutations(numbers, i):
            s = int(''.join(x))
            if (s in primes):
                answer.add(s)
        
    return len(answer)