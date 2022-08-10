##check

n = int(input())
A = list(map(int, input().split(' ')))
m = int(input())
B = list(map(int, input().split(' ')))


A.sort()

# 중복 숫자의 인덱스 범위 구하는것***
def bs(num, bound):
    start, end = 0, n
    while(start < end):
        mid = (start + end) // 2
        if bound == 0:# 중복 숫자의 낮은 인덱스
            if A[mid] < num:
                start = mid + 1
            else:
                end = mid
        else:# 중복 숫자의 높은 인덱스
            if A[mid] <= num:
                start = mid + 1
            else:
                end = mid
    return end

result = []
for i in B:
    #print(bs(i,1)) # 5 5 3 
    #print(bs(i,0)) # 5 3 0
    result.append(bs(i,1) - bs(i,0))
print(*result)