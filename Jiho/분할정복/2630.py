import sys
input=sys.stdin.readline
n=int(input())
color_paper=[]
for i in range(n):
    color_paper.append(list(map(int,input().split())))
def solve(arr):
    if len(arr)==1:
        if arr[0][0]==1:
            return (0,1)
        else:
            return (1,0)
    
    is_same=True
    target=arr[0][0]
    for elems in arr:
        flag=False
        for elem in elems:
            if elem != target:
                is_same = False        
                break
        if not is_same:
            break 
    if is_same:
        if target==0:
            return (1,0)
        else:
            return (0,1)
    a = []
    b = []
    c = []
    d = []
    for i in range(len(arr)):
        if i < len(arr)/2:
            a.append(arr[i][:len(arr)//2])
            b.append(arr[i][len(arr)//2:])
        else:
            c.append(arr[i][:len(arr)//2])
            d.append(arr[i][len(arr)//2:])
    a1 = solve(a)
    b1 = solve(b)
    c1 = solve(c)
    d1 = solve(d)
    white = a1[0]+b1[0]+c1[0]+d1[0]
    blue = a1[1]+b1[1]+c1[1]+d1[1]
    return (white,blue)

white,blue = solve(color_paper)
print(white)
print(blue)
