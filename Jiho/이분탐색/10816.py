# 숫자 카드 2
#python3 시간초과
import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
m = int(input())
inputs = list(map(int, input().split()))
arr.sort()

result = []
length = len(arr)
for elem in inputs:
    left = 0
    right = length-1
    count=0
    while left <= right:
        mid = (left+right)//2
        if arr[mid]==elem:
            i=1
            j=1
            while mid-i>=left:
                if arr[mid-i]!=elem:
                    break
                i+=1
            while mid+j<=right:
                if arr[mid+j]!=elem:
                    break
                j+=1
            count=i+j-1
            break
        elif arr[mid]>elem:
            right=mid-1

        else:
            left=mid+1
    result.append(count)
for elem in result:
    print(elem,end=" ")