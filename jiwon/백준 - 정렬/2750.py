n = int(input())
arr = [int(input()) for _ in range(n)]

arr.sort()
arr2 = list(set(arr))

for i in arr2:
    print(i)
