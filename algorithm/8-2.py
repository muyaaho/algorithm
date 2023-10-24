# 피보나치 수열 메모이제이션(Memoization) 하기 위한 리스트
d = [0]*100

# 피보나치 수열을 재귀함수로 구현(탑다운 다이나믹 프로그래밍)
def fibo(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

print(fibo(99))

