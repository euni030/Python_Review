import tkinter as tk

def Sum(m, n):                      # Sum 함수 : 일반 함수와 동일함
    print("합계 : ", sum(range(m, n + 1)))

window = tk.Tk()                # 윈도우 창 만들기
button = tk.Button(window, text="클릭하세요!", command=lambda: Sum(1, 10))
button.pack()                   # window 창에 실제 배치

window.mainloop()               # 메시지 루프 구동
