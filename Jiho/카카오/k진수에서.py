import math

# 소수 판별 함수
def is_prime(n):
    if n == 1:
        return False
    
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
        
    return True

def solution(n, k):
    
    answer = 0
    #k진수로 변환한 숫자를 담는 변수 
    number=""
    
    #진수 변환 과정
    q = n 
    while(True):  
        r = q % k
        number = str(r) + number
        q = q // k
        
        #몫이 k보다 작으면 break
        if q < k:
            number = str(q) + number
            break
    
    # 0을 기준으로 숫자 나누기
    number_list=number.split('0')
    
    # number_list에 ''요소가 있으면 삭제
    while True:
        if '' in number_list:
            number_list.remove('')
        else:
            break
    
    #map을 통하여 문자열을 정수로 변환
    numbers = list(map(int,number_list))
    
    #소수 판별
    for elem in numbers:
        if is_prime(elem):
            answer+=1
            
    return answer