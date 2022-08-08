## 풀이중

N = int(input())
N_card = map(int, input().split(' '))
M = int(input())
M_card = map(int, input().split(' '))
answer = 0
N.sort() # -10 -10 2 3 3 6 10 10 10 


def solution(target):
    left = 0
    right = M-1
    answer = 0
    mid = (left+right)//2
    cnt = 0
    turn = 0  
            
    while target:
        for i in N_card:
            if target == i:
                cnt +=1 #3
        if cnt == 1:
             if target == N_card[mid]:
                answer +=1
                return True
        else: 
            if turn == cnt:
                if target == N_card[mid]: #10 == 10 
                    answer +=1 
                    return True
        if target > N_card[mid]: # 10 > 2
            left = mid+1 # 6 
        elif target < N_card[mid]:
            right = mid-1 # 4
           
    return answer
    
    
for i in M:
    if solution(i):
        print(answer)
    else:
        print(0)
        
         
    
