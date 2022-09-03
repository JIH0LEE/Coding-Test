def solution(id_list, report, k):
    
    answer=[]
    
    #유저의 신고받은 횟수를 저장하는 딕셔너리
    report_dic=dict()
    
    #딕셔너리에 0값으로 초기화
    for elem in id_list:
        report_dic[elem]=0
    
    #report의 중복을 제거하기 위한 집합
    report_set=set()
    
    #중복 제거
    for elem in report:
        report_set.add(elem)
    
    #report 딕셔너리에 값 추가
    for report_elem in report_set:
        a,b = report_elem.split(" ")
        report_dic[b]+=1
    
    #나쁜사람 담는 리스트
    nappen=[]
    
    #딕셔너리 돌면서 신고 횟수 k번 이상인 유저 나쁜 리스트에 넣기
    for key,value in report_dic.items():
        if value>=k:
            nappen.append(key)

    #유저를 한명씩 확인하면서 나쁜사람 신고 횟수만큼 answer에 담아줌
    for user in id_list:
        temp=0
        for nappen_elem in nappen:
            if user+" "+nappen_elem in report_set:
                temp+=1
        answer.append(temp)
                

    return answer