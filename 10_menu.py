import time 
from tkinter import * 
import tkinter.ttk as ttk 

root = Tk() 
root.title("Nado GUI") 
root.geometry("640x480") 

def creat_new_file() :
    print("making new file...")

menu = Menu(root)  

menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="New File", command=creat_new_file)
menu_file.add_command(label="New Window") 
menu_file.add_separator() 
menu_file.add_command(label="Open File...") 
menu_file.add_separator() 
menu_file.add_command(label="Save All", state="disable") 
menu_file.add_separator() 
menu_file.add_command(label="Exit", command=root.quit) 


menu.add_cascade(label="File", menu=menu_file) 

menu.add_cascade(label="Edit") 

# Radio button
menu_lang = Menu(menu, tearoff=0)
menu_lang.add_radiobutton(label="Python")
menu_lang.add_radiobutton(label="Java")
menu_lang.add_radiobutton(label="C++")
menu.add_cascade(label="Language", menu=menu_lang)

# check button
menu_view = Menu(menu, tearoff=0)
menu_view.add_checkbutton(label="Show Minimap")
menu.add_cascade(label="View", menu=menu_view)


root.config(menu=menu) 

root.mainloop()