k, n = map(int, input().split())
kArr =[int(input()) for _ in range(k)]


min = 1
max =max(kArr)
answer =0

while min <= max: 
    
    mid= (min+max)//2
    cnt =0 
    for i in kArr: 
        cnt += i // mid 
        
    if(cnt>=n):
        answer = mid  #!!!!!!
        min = mid +1 
    
    elif(cnt<n):
        max = mid-1   
        
print(answer)
    
# k,n,kArr 입력받기
# 랜선 최소길이 1, 최대길이는 가지고있는 것 max
# while 사용( start<= end)
# 이진탐색 중간값 선언
# 중간값으로 랜선잘라보고 몇 개 생기는 지 count
# 그 카운트값이 n보다 작으면 더 길게 잘라야함 mid+1
# 반대면 mid-1
# start<=end 지점까지 반복하면 cnt>=n 이 되는 지점에 , 답나옴








