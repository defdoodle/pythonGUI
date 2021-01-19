import os
from tkinter import *

root = Tk()
root.title("Window 메모장")
root.geometry("640x480")

menu =  Menu(root)

frame = Frame(root)
frame.pack(expand=True, fill="both")

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

text = Text(frame, yscrollcommand=scrollbar.set)
text.pack(expand=True, fill="both")

filename = "mynote.txt"


def open_file() :
    if os.path.isfile(filename) :
        with open(filename, "r", encoding="utf8") as file : 
            text.delete("1.0", END)
            text.insert(END, file.read())

    
def save_file() :
    with open(filename, "w", encoding="utf8") as file : 
        file.write(text.get("1.0", END))
    

menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="열기", command=open_file)
menu_file.add_command(label="저장", command=save_file)
menu_file.add_separator() 
menu_file.add_command(label="끝내기",command=root.quit)


menu.add_cascade(label="파일", menu=menu_file)
menu.add_cascade(label="편집")
menu.add_cascade(label="서식")
menu.add_cascade(label="보기")
menu.add_cascade(label="도움말")

root.config(menu=menu)
scrollbar.config(command=text.yview)

root.mainloop()