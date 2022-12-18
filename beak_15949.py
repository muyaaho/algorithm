''' 참고
https://jiwon-coding.tistory.com/21
https://chanhuiseok.github.io/posts/algo-23/
https://gmlwjd9405.github.io/2018/08/14/algorithm-dfs.html
'''

n, m = map(int, input().split())

arr = []
def back():
    if len(arr) == m:
        print(*[arr[i] for i in range(m)])
    
    else:
        for i in range(1, n+1):
            if i not in arr:
                arr.append(i)
                back()
                arr.pop()

back()