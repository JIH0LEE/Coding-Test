n,k = map(int, input().split(' '))
arr = list(map(int, input().split(' ')))

arr.sort(reverse=True)
num = 0
for i in range(n):
  if i+1 == k:
    print(arr[i])
