
N = int(input())
A = list(map(int, input().split(' ')))
A.sort()
#12345
M = int(input())
B = list(map(int, input().split(' ')))

def solution(target):
    left = 0
    right = N-1
    
    while left <= right:
        mid = (left + right) //2 # mid =5 
        if target == A[mid]: # B[5]
            return True
        # 10 > 5     //       123456789,44
        if target > A[mid]:  # B[5]
             left = mid+1 # 0 = 5+1 =6
        # 5 < 8
        elif target < A[mid]:
            right = mid-1  # 9 = 5-1 =4

for i in range(M):
    if solution(B[i]) :
        print(1)
    else:
        print(0)
                
