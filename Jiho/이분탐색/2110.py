#공유기 설치
import sys
input=sys.stdin.readline
n,c=map(int,input().split())
house=[0 for i in range(n)]
for i in range(n):
    house[i]=int(input())
house.sort()
left=1
right=house[-1]-house[0]
result=0
while left<=right:
    count=1
    mid=(left+right)//2
    before=house[0]
    for i in range(1,n):
        if house[i]>=before+mid:
            count+=1
            before=house[i]
        
    if count>=c:
        left=mid+1
        result=mid
    else:
        right=mid-1

print(result)