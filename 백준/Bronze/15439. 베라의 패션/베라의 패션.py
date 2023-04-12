from itertools import permutations

n = int(input())
print(len(list(permutations(range(n), 2))))
