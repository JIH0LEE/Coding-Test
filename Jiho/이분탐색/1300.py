#k 번째 수
# 메모리 초과 
import sys
input=sys.stdin.readline
n=int(input())
k=int(input())
left=1
right=k
result=0
while left<=right:
    mid=(left+right)//2
    cnt=0
    for i in range(1,n+1):
        cnt+=min(mid//i,n)
    if cnt>=k:
        right=mid-1
        result=mid
    else:
        left=mid+1
print(result)
