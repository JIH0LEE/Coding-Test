#프로그래머스
#탐욕법
#구명보트

#투포인터

def solution(people, limit):
    answer = 0
    people.sort()
    left=0
    right=len(people)-1
    while(left<right):
        if people[left]+people[right]<=limit:
            left+=1
            right-=1
            answer+=1
        else:
            right-=1
            answer+=1
        if left==right:
            answer+=1
            break
        
    print(people)
    return answer