#프로그래머스
#완전탐색
#카펫

import math

def solution(brown, yellow):
    answer = []
    sum=brown+yellow
    for i in range(3,round(math.sqrt(sum))+1):
        if sum%i==0:
            h=i-2
            w=sum//i-2
            if h*w==yellow:
                answer.append(w+2)
                answer.append(h+2)
    return answer