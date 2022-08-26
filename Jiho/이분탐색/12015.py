#가장 긴 증가하는 부분수열 2
#구글링 함
#해당 배열은 구할 수 없지만 길이는 변하지 않음
import sys
from bisect import bisect_left

input=sys.stdin.readline
n=int(input())
inputs=list(map(int,input().split()))
result=[0]
for elem in inputs:
    if elem>result[-1]:
        result.append(elem)
    else:
        
        result[bisect_left(result,elem)]=elem
print(len(result)-1)