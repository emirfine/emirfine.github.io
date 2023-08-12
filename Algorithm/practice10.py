def solution(emergency):
    answer = [0 for _ in emergency] # result
    
    # 어떻게?
    # 정렬?
    
    # 정석대로?
    # 1. emergency를 정렬한 배열을 새로 만든다. (내림차순)
    # 2. index를 찾는다.
    # 3. 해당 위치에, 현재 몇 번째 응급도가 높은 환자인지 넣어준다.
    sorted_list = sorted(emergency, reverse=True)
    # print(sorted_list)
    for order, e in enumerate(sorted_list):
        idx = emergency.index(e)
        answer[idx] = order + 1
    
    answer = [sorted(emergency, reverse=True).index(e)+1 
     for e in emergency]
        
    return answer