import tkinter as tk
window=tk.TK()

button_text== [['7',  '8',  '9',  '/',  'C'],
               ['4',  '5',  '6',  '*'],
               ['1',  '2',  '3',  '-'],
               ['0',  '.',  '=',  '+']]

for i in range(1,5):
    window.rowconfigure(i,weight=1)

for i in range(5):
    window.columnconfigure(i, wiehgt=1)

entry=tk.Entry(window)
entry.grid(row=0,column=0, columnspan=5)

for i in range(len(button_text)):
    for j in range(len(button_text[i])):
        tk.Button(window, text=button_text[i][j]).grid(row=i+1,column=j,sticky=tk.E+tk.W+tk.S+tk.N)

window.mainloop()