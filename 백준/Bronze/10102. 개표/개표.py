n = int(input())
a = input()

if a.count('A') > a.count('B'):
    print('A')
elif a.count('A') == a.count('B'):
    print('Tie')
else:
    print('B')