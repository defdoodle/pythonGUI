from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

chkvar = IntVar() #chkvar에 int 형으로 값을 저장한다
chkbox = Checkbutton(root, text="오늘 하루 보지 않기", variable=chkvar)
#chkbox.select() # auto select
#chkbox.deselect() # auto deselect
chkbox.pack()

chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text="일주일 동안 보지않기", variable=chkvar2)
chkbox2.pack()

def btncmd() :
    print(chkvar.get()) # 0 : checked, 1 : unchecked
    print(chkvar2.get())


btn = Button(root, text="CLICK!!!", command=btncmd)
btn.pack()

root.mainloop()