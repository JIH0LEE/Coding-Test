#프로그래머스
#완전 탐색
#소수 찾기
import sys
import math

number=""

def brute_force(cnt,max_length,available,num_set):
    
    global number
    
    #입력받은 문자열보다 길이가 길면 return
    if cnt==max_length+1:
        return
    
    #만든 숫자를 집합에 추가
    if number!="":
        num_set.add(int(number))
        
    #브루트포스 
    for i in range(len(available)):
        
        number+=available[i]
        
        next_available=available[:]

        del next_available[i]

        brute_force(cnt+1,max_length,next_available,num_set)
        
        number=number[:-1]
        

#소수 판별
def is_prime(num):
    if num<=1:
        return False
    for i in range(2,round(math.sqrt(num))+1):
        if num%i==0:
            return False
    return True
    
    

def solution(numbers):
    
    num_set=set()
    
    available=list(numbers)
    
    brute_force(0,len(numbers),available,num_set)
    
    answer = 0
    
    for elem in num_set:
        if is_prime(elem):
            answer+=1
            
    return answer