import tkinter as tk

def OntextAddButton():
    text.insert(tk.END, entry.get())

def OntextAutoAddButton():
    text.insert(tk.END, "\n"+entry.get())

def OnDeleteButtonClick():
    entry.delete(0, tk.END)

def OntextDeleteButton():
    text.delete(1.0, tk.END)

window = tk.Tk()
window.title("tkinter GUI")

entryFrame = tk.Frame(window)
entryFrame.pack(side=tk.TOP, fill=tk.BOTH)

entry = tk.Entry(entryFrame)
entry.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

EntrydeleteButton = tk.Button(entryFrame, text="엔트리 삭제", command=OnDeleteButtonClick)
EntrydeleteButton.pack(side=tk.LEFT, padx = 5, pady = 5, ipady = 5)

button1 = tk.Button(window, text="엔트리 내용을 텍스트로 추가하기", command=OntextAddButton)
button1.pack(side=tk.TOP, fill=tk.BOTH, padx = 5, pady = 1, ipady = 5)

button2 = tk.Button(window, text="엔트리 내용을 텍스트로 추가하기(다음 줄 자동 추가)", command=OntextAutoAddButton)
button2.pack(side=tk.TOP, fill=tk.BOTH, padx = 5, pady = 1, ipady = 5)

outputFrame = tk.Frame(window)
outputFrame.pack(side=tk.TOP, expand=1, fill=tk.BOTH, padx = 5, pady = 5)

textDeleteButton = tk.Button(outputFrame, text="텍스트 삭제", command=OntextDeleteButton)
textDeleteButton.pack(side=tk.LEFT, fill=tk.BOTH, padx = 5, pady = 5)

text = tk.Text(outputFrame, width=30, height=10)
text.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

window.mainloop()