#실행이 제대로 안됨ㅠ
import turtle

# 초기 설정
turtle.setup(800, 600)  # 윈도우 크기 설정
turtle.title("거북이 그림판")  # 윈도우 제목 설정
turtle.speed(0)  # 거북이 속도 최대로 설정

# 펜 설정
t = turtle.Pen()
t.pensize(3)  # 펜 굵기 설정
t.speed(0)  # 펜 속도 최대로 설정

# 마우스 이벤트 처리 함수
def draw(x, y):
    # 마우스 왼쪽 버튼이 눌린 경우에만 그림 그리기
    if t.isdown():
        t.goto(x, y)

# 마우스 클릭 이벤트 처리 함수
def click(x, y):
    if t.isdown():
        t.penup()
    else:
        t.pendown()
        t.goto(x, y)

# 마우스 이벤트 처리 함수 등록
t.ondrag(draw)
t.onclick(click,1)

turtle.done()  # 윈도우 이벤트 루프 시작
