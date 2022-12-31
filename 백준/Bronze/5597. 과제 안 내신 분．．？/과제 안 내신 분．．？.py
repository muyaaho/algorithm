student = [int(input()) for _ in range(28)]
student.sort

for num in range(1, 31):
    if num not in student:
        print(num)