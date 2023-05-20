import tkinter as tk

window=tk.Tk()
entry1=tk.Entry(window)
entry1.pack()
label_plus=tk.Label(window,tet="+")
label_plus.pack()
entry2=tk.Entry(window)
entry2.pack()

def Sum():
    num1=float(entry1.get())
    num2=float(entry2.get())
    num3=num3+num2
    label_result.config(text=str(num3))
        
button=tk.Button(window, text="합계 계산", command=Sum)
button.pack()

label_result=tk.Label(window, text="0")
label_result.pack()

window.mainloop()

