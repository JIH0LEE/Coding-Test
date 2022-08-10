# N, M, 배열을 입력받는다.
N,M = map(int, input().split())
arr = list(map(int, input().split()))

#절단기의 최소 최대값
min = 0
max = max(arr)


#while 사용
while min <= max:
    temp =0
    #중간값
    mid = (min + max) // 2
    for i in arr:  #나무길이들
        if i>= mid: # 중간값보다 크면,!!!!!!!!!!!
            temp +=i-mid #높이만큼 자른거 합친다.
            
    # 구해야할 나무길이보다 작으면 /높이 낮춰야함     
    if temp <M: 
        max = mid -1
    # 구해야할 나무길이보다 크면 / 높이 크게 해야함
    elif temp >=M: 
        min = mid +1  
print(max)