#백준
#이분탐색
#수 찾기

import sys
input=sys.stdin.readline

def binary_search(target,a):
    left=0
    right=len(a)-1
    while left<=right:
        mid=(left+right)//2
        comp=a[mid]
        if comp==target:
            print(1)
            return
        elif comp<target:
            left=mid+1
        else:
            right=mid-1
    print(0)


n=int(input())
a=list(map(int,input().split()))
a.sort()
m=int(input())
b=list(map(int,input().split()))
for num in b:
    binary_search(num,a)