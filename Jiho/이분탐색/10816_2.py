# 숫자 카드 2
# dictionary 사용
import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
m = int(input())
inputs = list(map(int, input().split()))
count_dict = dict()
result=[0 for i in range(m)]
for elem in arr:
    if elem in count_dict:
        count_dict[elem]+=1
    else:
        count_dict[elem]=1

for i in range(len(inputs)):
    if inputs[i] in count_dict:
        result[i]=count_dict[inputs[i]]
for elem in result:
    print(elem,end=" ")
