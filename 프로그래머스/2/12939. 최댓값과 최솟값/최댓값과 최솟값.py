def solution(s):
    number_list =  list(map(int,s.split()))
    number_list.sort()
    
    answer = ''
    answer += str(number_list[0])+ " " + str(number_list[-1])
    return answer