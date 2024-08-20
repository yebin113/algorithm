def solution(progresses, speeds):
    N = len(speeds)
    answer = []
    end_time = [0]*N
    for i in range(N):
        end_time[i] = (100-progresses[i]) // speeds[i]
        if speeds[i] != 1 and (100-progresses[i]) % speeds[i]:
            end_time[i] += 1
    print(end_time)
    
    
    visited = [0]*N
    for i in range(N):
        cnt = 0
        if visited[i]:
            continue
        for j in range(i,N):
            if end_time[i] >= end_time[j]:
                cnt += 1
                visited[j] = 1
            else:
                break
        answer.append(cnt)
        
        
        
        
    return answer