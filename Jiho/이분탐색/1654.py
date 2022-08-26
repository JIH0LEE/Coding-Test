#랜선 자르기
import sys
input=sys.stdin.readline
k,n=map(int,input().split())
inputs=[0 for i in range(k)]
for i in range(k):
    inputs[i]=int(input())
left=1
right=max(inputs)
max_len=0
while left<=right:
    count=0
    mid=(left+right)//2
    for elem in inputs:
        count+=elem//mid

    if count<n:
        right=mid-1
    else:
        
        max_len=mid
        left=mid+1

print(max_len)

