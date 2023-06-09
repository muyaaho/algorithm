a, b = input().split()

small, large = 0, 0

# 작은 수 버전
if "6" in a:
    a = a.replace("6", "5")
if "6" in b:
    b = b.replace("6", "5")

small = int(a)+int(b)

# 큰 수 버전
if "5" in a:
    a = a.replace("5", "6")
if "5" in b:
    b = b.replace("5", "6")

large = int(a)+int(b)

print(small, large)


