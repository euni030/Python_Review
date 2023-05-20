import tkinter as tk

window=tk.Tk()
canvas=tk.Canvas(window, width=300,height=200, b="white")
canvas.pack(expand=1, fill=tk.BOTH)

def DrawShape():
    canvas.delete(tk.ALL)
    color="red" if var_fill.get()=="yes" else None
    if var_shape.get()==1:
        canvas.create_rectangle(10,10,290,190,fill=color)
    else:
       canvas.create_oval(10,10,290,190,fill=color)

var_shape=tk.IntVar(window,1)
radio_rect=tk.Radiobutton(window, text="사각형", value=1, variable=var_shape, command=DrawShape)
radio_rect.pack(side=tk.LEFT)
radio_oval=tk.Radiobutton(window, text="타원", value=2, variable=var_shape, command=DrawShape)
radio_oval.pack(side=tk.LEFT)

var_fill=tk.StringVar(window,"no")
check_fill=tk.Checkbutton(window, text="채움 여부", onvalue="yes", offvalue="no", variable=var_fill)
check_fill.pack(side=tk.RIGHT)

window.mainloop()