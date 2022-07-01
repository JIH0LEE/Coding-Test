#프로그래머스
#탐욕법
#체육복
def solution(n, lost, reserve):
    
    clothes=[1]*n

    print(clothes)
    answer = 0
    for elem in lost:
        clothes[elem-1]=0
        
    for elem in reserve:
        clothes[elem-1]+=1
    print(clothes)
    for idx,student in enumerate(clothes):
        if student==0:
            if idx==0:
                if clothes[idx+1]==2:
                    clothes[idx]=1
                    clothes[idx+1]-=1
            elif idx==n-1:
                if clothes[idx-1]==2:
                    clothes[idx]=1
                    clothes[idx-1]-=1
            else:
                if clothes[idx-1]==2:
                    clothes[idx]=1
                    clothes[idx-1]-=1
                    continue
                if clothes[idx+1]==2:
                    clothes[idx]=1
                    clothes[idx+1]-=1
                    continue
    for elem in clothes:
        if elem>0:
            answer+=1
                     

    print(clothes)
    return answer


solution(5,[2,4],[1,3,5])