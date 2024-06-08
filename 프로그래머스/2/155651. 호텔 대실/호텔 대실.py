from datetime import datetime, timedelta

# datetime 변환 후
# 시작시간을 기준으로 정렬
# for문을 통해서 반복
    # 1depth list의 끝(-1) 조회 
        # 앞선 일정의 종료시간과 겹치면 1depth 방 하나 생성 (list append)
        # 기존 일정과 겹치지 않는다면 기존 2depth 리스트에 일정 추가 (list append)
# 2depth 갯수 리턴

def solution(book_time):
    room_list = []
    
    book_time.sort(key = lambda x: x[0])
    for i, time in enumerate(book_time):
        if i == 0:
            room_list.append([time])
        else:
            for room in room_list:
                _book_start_time = datetime.strptime(time[0], "%H:%M")
                _latest_room_finish_time = datetime.strptime(room[-1][1], "%H:%M")
                if _book_start_time >= _latest_room_finish_time + timedelta(minutes=10):
                    room.append(time)
                    break
            else:
                room_list.append([time])
        # room_list.sort(key = lambda x: x[-1][1])
    return len(room_list)