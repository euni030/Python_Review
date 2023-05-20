#사진 보고 고치기 ㅇㅇ


import tkinter as tk

def Change():
    img = tk.PhotoImage(file="python.png")
    label.config(image=img)                     # 이미지 파일 교체
    label.image = img   # label의 새로운 속성(image)에 대입 => 사라지지 않음
    # img 변수는 지역 변수이므로. 또는 global img와 같이 전역 변수로 선언
window = tk.Tk()
photo = tk.PhotoImage(file="language.gif")      # PhotoImage 객체 생성
label = tk.Label(window, image=photo)           # 레이블 위젯에 표시
label.pack()

button = tk.Button(window, text='그림 변경', command=Change)
button.pack()
window.mainloop()
