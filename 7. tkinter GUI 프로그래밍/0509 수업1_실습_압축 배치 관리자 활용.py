import tkinter as tk
window = tk.TK()

frame1=tk.Frame(window)
frame1.pack(fill=tk.BOTH)
label=tk.label(frame1,text="화씨", width=0)
label.pack(side=tk.LEFT)
entry=tk.Entry(frame1)
entry.pack(side=tk.LEFT, expand=1, fill=tk.BOTH)

frame2=tk.Frame(window)
frame2.pack(fill=tk.BOTH, expand=1)
button1=tk.Button(frame2, text="버튼1")
button1.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
button1=tk.Button(frame2, text="버튼2")
button1.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

window.mainloop()