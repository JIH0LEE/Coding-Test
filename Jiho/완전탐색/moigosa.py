#프로그래머스
#브루트포스
#모의고사

import sys

def solution(answers):
    answer = []
    #수포자들 답안
    supoja=[[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]
    
    #각각 정답 횟수
    count=[0,0,0]
    
    #정답 여부 확인
    for idx,elem in enumerate(answers):
        if supoja[0][idx%5]==elem:
            count[0]+=1
        if supoja[1][idx%8]==elem:
            count[1]+=1    
        if supoja[2][idx%10]==elem:
            count[2]+=1
            
    #가장 많이 맞춘 답안 개수
    max_supoja=max(count)
    
    #가장 많이 맞춘 사람 찾기
    for i in range(3):
        if count[i]==max_supoja:
            answer.append(i+1)

    return answer