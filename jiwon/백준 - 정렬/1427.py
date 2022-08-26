arr = list(map(int,input()))


arr.sort(reverse=True)

a =''
for i in arr:
  if(len(arr)>0):
    a+=''
  a+= str(i)
print(a)