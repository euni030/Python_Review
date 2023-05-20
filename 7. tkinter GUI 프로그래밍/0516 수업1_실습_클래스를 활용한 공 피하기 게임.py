import tkinter as tk
window=tk.Tk()

canvas=tk.Canvas(window, width=400, height=200, bg="white")
canvas.pack(expand=1, fill=tk.BOTH)
circle=canvas.create_oval(10,50,60,100,fill="red")

speed_x=10
speed_y=0

def MoveCircle():
    global speed_x
    #현재 위치
    x1,y1,x2,y2=canvas.coords(circle)
    #윈도우의 가로 길이
    window_width=window.winfo_width()
    print(x2, window_width)
    if x2>window_width or window_width!=1:
        speed_x=-10
    
    if x1<0:
        speed_x=10

    canvas.move(circle, speed_x, speed_y)  #오른쪽으로 10픽셀 이동
    window.update()
    canvas.after(100,MoveCircle)  #0.1초 간격으로 MoveCircle 함수 실행
    
   


MoveCircle()  #MoveCircle함수 최초 실행
window.mainloop()