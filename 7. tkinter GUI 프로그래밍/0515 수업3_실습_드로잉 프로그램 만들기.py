import tkinter as tk
window=tk.Tk()

canvas=tk.Canvas(window, width=600, height=400, bg="white")
canvas.pack(expand=1,fill=tk.BOTH)

def StartDraw(event):
    global x,y
    x=event.x
    y=event.y

canvas.bind("<Button-1>", StartDraw)


def MoveDraw(event):
    global x,y
    canvas.create_line( x,y,event.x, event.y)
    x=event.x
    y=event.y

canvas.bind("<B1-Motion>",MoveDraw)

window.bind("<Escape>",lambda event: canvas.delete((tk.ALL)))

window.mainloop()