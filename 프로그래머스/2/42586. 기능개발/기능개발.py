# 첫번째 배포 후 두번째 기능 배포 가능

def solution(progresses, speeds):
    answer = []
    
    while len(progresses) > 0:
        deploy = 0
        flag = True
        for i, _ in enumerate(progresses):
            progresses[i] += speeds[i]
            if flag and progresses[i] >= 100:
                deploy += 1
            else:
                flag = False
        progresses = progresses[deploy:]
        speeds = speeds[deploy:]
        if deploy > 0:
            answer.append(deploy)
    return answer
