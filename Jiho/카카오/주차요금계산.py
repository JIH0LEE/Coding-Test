
import math

#시간 계산
# elem EX) {("IN","6:00),("OUT","8:00")}
# elem EX) {("IN","4:20)}
def calculate_time(elem):
    
    #마지막 out기록 없으면 out 기록 추가
    if len(elem)%2==1:
        elem.append(("OUT","23:59"))
    
    result=0
    #분으로 환산해서 누적시간 계산
    for i in range(0,len(elem),2):
        start_hour,start_minute = elem[i][1].split(":")
        end_hour,end_minute = elem[i+1][1].split(":")
        result+=(int(end_hour)*60+int(end_minute)-int(start_hour)*60-int(start_minute))

    return result
    
    
def solution(fees, records):
    
    basic_time=fees[0]
    basic_price=fees[1]
    unit_time=fees[2]
    unit_price=fees[3]
    
    #차량마다 입차 출차 기록 넣기 위한 딕셔너리
    time_dic=dict()
    
    #딕셔너리에 차량 입-출차 기록 저장
    for record in records:
        time,idx,op = record.split(" ")
        if idx not in time_dic.keys():
            time_dic[idx]=[]
            time_dic[idx].append((op,time))
        else:
            time_dic[idx].append((op,time))
            
    answer = []
    
    #출력은 차량번호가 작은 순으로 출력해야함. 따라서 sort해줬음 
    sorted_dict=sorted(time_dic.items())
    
    #차량마다 시간 구해서 금액 계산 후 answer에 넣음
    for elem in sorted_dict:
        time = calculate_time(elem[1])
        if time<=basic_time:
            answer.append(basic_price)
        else:
            answer.append(basic_price+(math.ceil((time-basic_time)/unit_time))*unit_price)
    
    return answer