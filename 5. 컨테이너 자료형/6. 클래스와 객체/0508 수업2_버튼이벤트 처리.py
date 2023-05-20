import tkinter as tk

def Sum():                      # Sum 함수 : 일반 함수와 동일함
    sum = 0
    for i in range(1, 11):
        sum += i
    print("합계 : ", sum)

window = tk.Tk()                # 윈도우 창 만들기
button = tk.Button(window, text="클릭하세요!", 
                   command=Sum) # 클릭=>Sum 함수 실행
button.pack()                   # window 창에 실제 배치
window.mainloop()               # 메시지 루프 구동
