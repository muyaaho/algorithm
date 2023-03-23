from math import gcd

aj, am = map(int, input().split())
bj, bm = map(int, input().split())

m = am*bm//gcd(am, bm)
j = m//am*aj + m//bm*bj

print(j//gcd(j,m), m//gcd(j,m))
