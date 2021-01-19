from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

txt = Text(root, width=30, height=5)
txt.pack()
txt.insert(END, "글자를 입력하세요")

e = Entry(root, width=30)
e.pack()
e.insert(0, "type just one line!!!")

def btncmd() :
    #내용 출력   
    print(txt.get("1.0", END))  # 1 : first line, 0 : position of zeroth column
    print(e.get())

    #내용 삭제
    txt.delete("1.0", END)
    e.delete(0, END)

btn = Button(root, text="CLICK!!!", command=btncmd)
btn.pack()

root.mainloop()