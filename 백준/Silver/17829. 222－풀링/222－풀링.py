n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

def f(arr):
    if len(arr)==1:
        print(arr[0][0])
        # print('여기서 리턴함여:', arr[0][0])
        return None
    else:
        ans = []
        for x in range(0, len(arr)//2):
            ans.append([])
            for y in range(0, len(arr)//2):
                x2 = x*2
                y2 = y*2
                l1 = []
                # print(x, y)
                l1.extend(arr[x2][y2:y2+2])
                l1.extend(arr[x2+1][y2:y2+2])
                # print(l1)
                l1.sort()
                # print(l1)
                # print(l1[2])
                ans[x].append(l1[2])
            # print(ans)
        f(ans)

f(arr)