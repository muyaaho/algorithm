import sys
input = sys.stdin.readline

s = []
jungong = 0
gpa = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F': 0.0}

for _ in range(20):
    name, score, grade = input().rstrip().split()
    if grade != 'P':
        jungong += gpa[grade]*float(score)
        s.append(float(score))
    
print(jungong/sum(s))